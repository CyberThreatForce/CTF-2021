import pickle
import numpy as np
import imageio

def parse_gif_RGB(key, file='image'):
    lst_preds = []
    size = 512
    with open('network/trained_network.pkl', 'rb') as f:
        u = pickle._Unpickler(f)
        u.encoding = 'latin1'
        net = u.load()
    vect_pos = list(range(size**2))
    key_ascii = [str(ord(elt)) for elt in key]
    x = 0
    for i in range(size**2):
        x = (ord(key[i % len(key_ascii)]) + vect_pos[i] + x) % size**2
        vect_pos[i], vect_pos[x] = vect_pos[x], vect_pos[i]
    vect_adv_pos = vect_pos[:net.sizes[0]]
    with imageio.get_reader('chall2_flagged.png') as gif_reader:
        for i in range(gif_reader.get_length()):
            frame = gif_reader.get_data(i)
            reverted_adv_image = frame[:, :, 0].reshape(size ** 2)[vect_adv_pos]
            reverted_adv_image = (reverted_adv_image - reverted_adv_image.mean()) / reverted_adv_image.std()
            x = np.round(net.feedforward(reverted_adv_image.reshape(784, 1)), 2)
            lst_preds.append(str(np.argmax(x)))
    return lst_preds


if __name__ == '__main__':
    lst_preds = parse_gif_RGB('Dimitri_Kiriznov_403', file='chall2_flagged')
    print(''.join(lst_preds))
