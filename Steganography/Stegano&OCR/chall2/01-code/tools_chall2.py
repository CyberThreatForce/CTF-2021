#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 17:59:58 2021.

@author: tristantacule
"""

# %%
import os
import shutil
import re

import gzip
import pickle
import glob

import random
from random import randint

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from PIL import Image
import imageio
from apng import APNG


# %%
def load_backup(challpath):
    """Load back-up files.

    Load back-up images and gif.
    I made sure the back-ups work for the challenge so Its important to keep them.
    """
    # Removing the directories.
    # Note: I do not check if they exist or not, deal with it.
    shutil.rmtree(challpath / '03-img')
    shutil.rmtree(challpath / '04-res')

    _ = shutil.copytree(challpath / '99-backup/03-img', challpath / '03-img')
    _ = shutil.copytree(challpath / '99-backup/04-res', challpath / '04-res')


# %%
def vectorized_result(j):
    """Vectorize the result."""
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e


def load_data_wrapper(challpath):
    """Load the data."""
    # Load the dataset containing handwritten data.
    with gzip.open(challpath / '02-data/mnist.pkl.gz', 'rb') as f:
        u = pickle._Unpickler(f)
        u.encoding = 'latin1'
        tr_d, va_d, te_d = u.load()
        f.close()

    # A bit of formatting to get each image with its label.
    training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = list(zip(training_inputs, training_results))
    validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
    validation_data = list(zip(validation_inputs, va_d[1]))
    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_data = list(zip(test_inputs, te_d[1]))

    return (training_data, validation_data, test_data)


def load_network(challpath):
    """Load the network."""
    # Simply load the network, its a bit convoluted as a workaround to some weird error.
    with open(challpath / '02-data/trained_network.pkl', 'rb') as f:
        u = pickle._Unpickler(f)
        u.encoding = 'latin1'
        net = u.load()

    return net


# %%
def sigmoid(z):
    """Return a sigmoid."""
    return 1.0/(1.0+np.exp(-z))


def sigmoid_prime(z):
    """Derive the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))


def input_derivative(net, x, y):
    """Calculate derivatives wrt the inputs."""
    nabla_b = [np.zeros(b.shape) for b in net.biases]
    nabla_w = [np.zeros(w.shape) for w in net.weights]

    # feedforward
    activation = x
    activations = [x]  # list to store all the activations, layer by layer
    zs = []  # list to store all the z vectors, layer by layer
    for b, w in zip(net.biases, net.weights):
        z = np.dot(w, activation)+b
        zs.append(z)
        activation = sigmoid(z)
        activations.append(activation)

    # backward pass
    delta = net.cost_derivative(activations[-1], y) * \
        sigmoid_prime(zs[-1])
    nabla_b[-1] = delta
    nabla_w[-1] = np.dot(delta, activations[-2].transpose())

    for layer in range(2, net.num_layers):
        z = zs[-layer]
        sp = sigmoid_prime(z)
        delta = np.dot(net.weights[-layer+1].transpose(), delta) * sp
        nabla_b[-layer] = delta
        nabla_w[-layer] = np.dot(delta, activations[-layer-1].transpose())

    # Return derivatives WRT to input
    return net.weights[0].T.dot(delta)


# %%
def adversarial(net, n, steps=1000, eta=1):
    """Create an adversial image.

    net : network object
        neural network instance to use
    n : integer
        our goal label (just an int, the function transforms it into a one-hot vector)
    steps : integer
        number of steps for gradient descent
    eta : float
        step size for gradient descent
    """
    # Set the goal output
    goal = np.zeros((10, 1))
    goal[n] = 1

    # Create a random image to initialize gradient descent with
    x = np.random.normal(.5, .3, (784, 1))

    # Gradient descent on the input
    for i in range(steps):
        # Calculate the derivative
        d = input_derivative(net, x, goal)

        # The GD update on x
        x -= eta * d

    return x


def simple_test(net, target, plot=True):
    """Perform a simple test of adversarial attack.

    n : integer
        Goal label (not a one hot vector).
    """
    # Create an adverse image and make a prediction on it.
    adv_image = adversarial(net, target)
    preds = np.round(net.feedforward(adv_image), 2)

    # Report on basic stuff : predicted probabilities, target vs prediction.
    print('Network Output:')
    print(' - '.join([str(elt) for elt in preds.reshape(len(preds))]))
    print(f'\nTarget: {target}')
    print(f'Network Prediction: {str(np.argmax(preds))}')

    # Ploting or not the image to get an idea of how it works.
    if plot:
        side = int(np.sqrt(net.sizes[0]))
        print('\nAdversarial Example: ')
        plt.imshow(adv_image.reshape(side, side), cmap='Greys')
        plt.show()


# %%
def get_shuffle(key, size):
    """Get the new place of each pixel. RC4."""
    vect_pos = list(range(size**2))
    x = 0
    for i in range(size**2):
        # x = (ord(key[i % len(key)]) + vect_pos[i] + x) & eval(hex(size**2 - 1))
        x = (ord(key[i % len(key)]) + vect_pos[i] + x) % size**2
        vect_pos[i], vect_pos[x] = vect_pos[x], vect_pos[i]

    return vect_pos


def get_shuffle_bis(key, size):
    """Get the new place of each pixel. RC4."""
    vect_pos = list(range(size**2))
    key_ascii = [str(ord(elt)) for elt in key]
    x = 0
    for i in range(size**2):
        x = (ord(key[i % len(key_ascii)]) + vect_pos[i] + x) % size**2
        vect_pos[i], vect_pos[x] = vect_pos[x], vect_pos[i]

    return vect_pos


def get_shuffle_RB(key, size):
    """Get the new place of each pixel. RC4."""
    vect_pos = list(range(2 * (size**2)))
    x = 0
    for i in range(2 * (size**2)):
        x = (ord(key[i % len(key)]) + vect_pos[i] + x) % size**2
        vect_pos[i], vect_pos[x] = vect_pos[x], vect_pos[i]

    return vect_pos


# %%
def gen_adv_images(net, target, challpath):
    """Generate adversarial images for a specific target."""
    # We try 100 times.
    for i in range(100):
        # We generate an adversarial image based on the target.
        adv_image = adversarial(net, target)

        # The prediction on the adversarial image itself is not used because, ultimately we need the modified
        # adversarial image to match the original target.
        # In some cases, the adverserial image does not match the target but the modified version does.
        # Example : target = 3.
        # The adversarial image gives 5 as a prediction.
        # The modified version gives 3.
        # It is a rare occurence but I've seen it happen.
        preds = np.round(net.feedforward(adv_image), 2)

        # We give the adversarial image the same treatment it will receve when integrated to the APNG.
        # Namely we convert it to 0 - 255 range then convert it back to 0 centered values.
        adv_image = ((adv_image - adv_image.min()) / (adv_image.max() - adv_image.min())) * 255
        adv_image = adv_image.astype(np.uint8)

        adv_image_bis = (adv_image - adv_image.mean()) / adv_image.std()
        preds2 = np.round(net.feedforward(adv_image_bis), 2)

        # In order to name the file, we count how many adversarial images for the same target already exist
        nb_offset = len(glob.glob(str(challpath / f'03-img_adv/adv_{target}*.png')))

        # Finaly, if the second prediction match the target, we can save the image.
        if str(np.argmax(preds2)) == str(target):
            im = Image.fromarray(adv_image.reshape(28, 28))
            im.save(challpath / f'03-img_adv/adv_{target}_{nb_offset:03}.png')

        # 5 adversarial image per target is more than enough.
        if nb_offset == 5:
            break


def test_adv_image(net, challpath, img_file):
    """Test if an adv image is indeed what it is supposed to be."""
    img = Image.open(challpath / f'03-img_adv/{img_file}')
    img = np.array(img)

    target = re.search(r'\_(\d)\_', img_file).group(1)

    # to the original format.
    img = img.reshape(len(img)**2, 1)
    img = (img - img.mean()) / img.std()

    # Then a prediction is made.
    x = np.round(net.feedforward(img), 2)
    pred = str(np.argmax(x))

    return target == pred


# %%
def gen_full_adverse(net, adv_target, vect_adv_pos, size):
    """Create a full sized adverse image."""
    # Create a small adverse image.
    adv_image = adversarial(net, adv_target)

    # Creating a full image of the final disered size.
    full_image = np.random.uniform(low=adv_image.min(), high=adv_image.max() - np.percentile(adv_image, 65), size=size**2)
    # The adversarial image is inserted into the full image.
    full_image[vect_adv_pos] = adv_image.reshape(len(adv_image))
    full_image = full_image.reshape(size**2, 1)

    # A bit of processing to be able to save the image as bitmap.
    full_image = (full_image - full_image.min())
    full_image = full_image / full_image.max()
    full_image = full_image * 255
    full_image = full_image.astype(np.uint8)

    return full_image


def purge_dirs(challpath, purge_img, purge_gif):
    """Purge dirs of images and gifs."""
    if purge_img:
        lst_img = os.listdir(challpath / '03-img')
        for img in lst_img:
            os.remove(challpath / f'03-img/{img}')

    if purge_gif:
        lst_gif = os.listdir(challpath / '04-res')
        for gif in lst_gif:
            os.remove(challpath / f'04-res/{gif}')


def gen_list_images(net, challpath, lst_img, size, vect_adv_pos):
    """Create a list of images."""
    # For every wanted predicted results (lst_img), an image is created and saved.
    for i, elt in enumerate(lst_img):
        # Creating an image with elt as a target.
        # Note that it does not work properly, but enough for the challenge.
        full_image = gen_full_adverse(net, elt, vect_adv_pos, size)

        im = Image.fromarray(full_image.reshape(size, size))
        im.save(challpath / f'03-img/result_{i:03}.png')


def gen_gif(net, challpath, size, imgs_to_gen, vect_adv_pos, purge_img=True, purge_gif=True):
    """Generate a gif."""
    # imgs_to_gen can be an int, in which case it represente the number of random image to create ...
    if isinstance(imgs_to_gen, int):
        lst_img = [randint(0, 9) for _ in range(imgs_to_gen)]
    # ... imgs_to_gen can also be a list of target for which we want an adverse image.
    else:
        lst_img = imgs_to_gen

    # Purge, or not the directories.
    purge_dirs(challpath, purge_img, purge_gif)

    # Creating the list of bse PNGs.
    gen_list_images(net, challpath, lst_img, size, vect_adv_pos)

    # Then the GIF is saved.
    img, *imgs = [Image.open(challpath / f) for f in sorted(glob.glob(str(challpath / '03-img/*.png')))]
    img.save(fp=challpath / '04-res/image.gif', format='GIF', append_images=imgs, save_all=True, duration=20, loop=0)


def parse_gif(net, challpath, size, vect_adv_pos, file='image'):
    """Parse a gif."""
    lst_preds = []
    with imageio.get_reader(challpath / f'04-res/{file}.gif') as gif_reader:
        for frame in gif_reader.iter_data():
            # For every frame of the gif, we have to inverse (as best we can) the transformation to get back
            # to the original format.
            frame = frame.reshape(size**2, 1)
            frame = (frame - frame.mean()) / frame.std()

            # Then a prediction is made.
            x = np.round(net.feedforward(frame[vect_adv_pos]), 2)
            lst_preds.append(str(np.argmax(x)))

    return lst_preds


def extract_adv_from_gif(net, challpath, size, vect_adv_pos, file='image'):
    """Parse a gif."""
    with imageio.get_reader(challpath / f'04-res/{file}.gif') as gif_reader:
        i = 0
        for frame in gif_reader.iter_data():
            # For every frame of the gif, we have to inverse (as best we can) the transformation to get back
            # to the original format.
            frame = frame.reshape(size**2, 1)

            # Then a prediction is made.
            frame = frame[vect_adv_pos]

            im = Image.fromarray(frame.reshape(28, 28))
            im.save(challpath / f'03-img_adv/result_{i:03}.png')
            i += 1


def check_int_in_gif(lst_preds):
    """Check if every number in 0 to 9 can be created with our images."""
    for i in range(10):
        list_res = [elt for elt in lst_preds if elt == str(i)]
        if list_res:
            print(f'{i} : ok')
        else:
            print(f'{i} not found')


def create_list_ind_flag(flag, lst_preds):
    """Create a list of index in order to create the flag.

    The goal is to get, for every character in the flag, the right image that code for this character.
    """
    df = pd.DataFrame(lst_preds)
    df.reset_index(inplace=True)
    df.columns = ['ind', 'val']

    lst_ind = []
    for char in flag:
        ind = df.loc[df['val'] == char].sample(1).index[0]
        lst_ind.append(ind)

    return lst_ind


def create_flagged_image(flag, lst_preds, challpath):
    """Create the flag in GIF form."""
    lst_ind = create_list_ind_flag(flag, lst_preds)

    lst_files = [challpath / f'03-img/result_{elt:03}.png' for elt in lst_ind]
    img, *imgs = [Image.open(f) for f in lst_files]
    img.save(fp=challpath / '04-res/flagged_image.gif', format='GIF', append_images=imgs, save_all=True, duration=20, loop=0)


def parse_flag(lst_preds):
    """Parse a ASCII flag."""
    flag = ''.join(lst_preds)
    parsed_flag = ''.join([chr(int(flag[i:(i + 3)])) for i in range(0, len(flag), 3)])
    return parsed_flag


# %%
def gen_full_adverse_rgb(net, adv_target, vect_adv_pos, size, bwimage=False):
    """Create a full sized adverse image in color."""
    # Creating the starting adversarial image.
    adv_image = adversarial(net, adv_target)

    # RGB need scaled values.
    adv_image = (adv_image - adv_image.min())
    adv_image = adv_image / adv_image.max()
    adv_image = adv_image * 120

    vect_adv_pos_R = [elt for elt in vect_adv_pos if elt < size ** 2]
    vect_adv_pos_B = [elt for elt in vect_adv_pos if elt >= size ** 2]

    if bwimage:
        full_image = np.zeros([size, size, 3], dtype=np.uint8)
    else:
        full_image = np.random.uniform(low=0, high=120, size=(size, size, 3))

    full_image[[elt // size for elt in vect_adv_pos_R],
               [elt % size for elt in vect_adv_pos_R], 0] =\
        adv_image[:len(vect_adv_pos_R)].reshape(len(vect_adv_pos_R))

    full_image[[(elt - size ** 2) // size for elt in vect_adv_pos_B],
               [(elt - size ** 2) % size for elt in vect_adv_pos_B], 2] =\
        adv_image[len(vect_adv_pos_R):].reshape(len(vect_adv_pos_B))

    full_image = full_image .astype('uint8')

    return full_image


def gen_full_adverse_rgb_alt(net, adv_image, vect_adv_pos, size, bwimage=False):
    """Create a full sized adverse image in color."""
    if bwimage:
        full_image = np.zeros([size ** 2, 3], dtype=np.uint8)
    else:
        full_image = np.random.uniform(low=0, high=120, size=(size ** 2, 3))
        full_image = full_image.astype(np.uint8)

    full_image[vect_adv_pos, 0] = adv_image.reshape(784)

    full_image.resize(size, size, 3)

    # full_image = full_image.astype('uint8')

    return full_image


def gen_list_images_RGB(net, challpath, lst_img, size, vect_adv_pos):
    """Create a list of images."""
    # For every wanted predicted results (lst_img), an image is created and saved.
    for i, elt in enumerate(lst_img):
        # Creating an image with elt as a target.
        # Note that it does not work properly, but enough for the challenge.
        full_image = gen_full_adverse_rgb(net, elt, vect_adv_pos, size, bwimage=False)

        im = Image.fromarray(full_image.reshape(size, size, 3))
        im.save(challpath / f'03-img/result_{i:03}.png')


def gen_list_images_RGB_from_lst_adv(net, challpath, flag, size, vect_adv_pos):
    """Create a list of images."""
    # For every wanted predicted results (lst_img), an image is created and saved.
    for i, elt in enumerate(flag):
        # Creating an image with elt as a target.
        files = glob.glob(str(challpath / f'03-img_adv/adv_{elt}*.png'))
        file = random.choice(files)

        img = Image.open(file)
        img = np.array(img)

        full_image = gen_full_adverse_rgb_alt(net, img, vect_adv_pos, size, bwimage=False)

        im = Image.fromarray(full_image.reshape(size, size, 3))
        im.save(challpath / f'03-img/result_{i:03}.png', lossless=True)


def gen_gif_RGB(net, challpath, size, imgs_to_gen, vect_adv_pos, purge_img=True, purge_gif=True):
    """Generate a gif."""
    # imgs_to_gen can be an int, in which case it represente the number of random image to create ...
    if isinstance(imgs_to_gen, int):
        lst_img = [randint(0, 9) for _ in range(imgs_to_gen)]
    # ... imgs_to_gen can also be a list of target for which we want an adverse image.
    else:
        lst_img = imgs_to_gen

    # Purge, or not the directories.
    purge_dirs(challpath, purge_img, purge_gif)

    # Creating the list of bse PNGs.
    gen_list_images_RGB(net, challpath, lst_img, size, vect_adv_pos)

    # Then the GIF is saved.
    img, *imgs = [Image.open(challpath / f) for f in sorted(glob.glob(str(challpath / '03-img/*.png')))]
    img.save(fp=challpath / '04-res/image.gif', format='GIF', append_images=imgs, save_all=True, duration=20, loop=0)


def gen_gif_RGB_from_list_adv(net, challpath, size, flag, vect_adv_pos, purge_img=True, purge_gif=True):
    """Generate a gif."""
    # Purge, or not the directories.
    purge_dirs(challpath, purge_img, purge_gif)

    # Creating the list of bse PNGs.
    gen_list_images_RGB_from_lst_adv(net, challpath, flag, size, vect_adv_pos)

    # Then the GIF is saved.
    # img, *imgs = [Image.open(challpath / f) for f in sorted(glob.glob(str(challpath / '03-img/*.png')))]
    # img.save(fp=challpath / '04-res/image.gif', format='GIF', append_images=imgs, save_all=True, duration=20, loop=0, lossless=True)

    # imgs = [Image.open(challpath / f) for f in sorted(glob.glob(str(challpath / '03-img/*.png')))]
    # lst_images = [np.array(elt) for elt in imgs]
    # clip = ImageSequenceClip(lst_images, fps=20)
    # clip.write_gif(challpath / '04-res/image.gif', fps=20)

    lst_files = sorted(glob.glob(str(challpath / '03-img/*.png')))
    APNG.from_files(lst_files, delay=100).save(challpath / '04-res/image.png')


def parse_gif_RGB(net, challpath, size, vect_adv_pos, file='image'):
    """Parse a gif."""
    lst_preds = []
    with imageio.get_reader(challpath / f'04-res/{file}.png') as gif_reader:
        # for frame in gif_reader.iter_data():
        for i in range(gif_reader.get_length()):
            frame = gif_reader.get_data(i)
            # For every frame of the gif, we have to inverse (as best we can) the transformation to get back
            # to the original format.
            reverted_adv_image = frame[:, :, 0].reshape(size ** 2)[vect_adv_pos]
            reverted_adv_image = (reverted_adv_image - reverted_adv_image.mean()) / reverted_adv_image.std()

            # Then a prediction is made.
            x = np.round(net.feedforward(reverted_adv_image.reshape(784, 1)), 2)
            # print(str(np.argmax(x)))
            lst_preds.append(str(np.argmax(x)))

    return lst_preds
