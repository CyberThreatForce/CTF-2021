def xor(cleartext,ciphertext):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#?!&%$-_1234567890"
    liste = []
    for i in cleartext:
        liste.append(alphabet.index(i))
    liste_bin=[]
    for i in liste:
        liste_bin.append(bin(i).split("b")[1])
    cipherbin = bin(int(ciphertext)).split("b")[1]*15
    liste_res = []
    for part in liste_bin:
        res = ""
        for index in range(len(part)):
            res += str(int(part[index])^int(cipherbin[index]))
        liste_res.append(res)
    liste_dec = []
    for i in liste_res:
        liste_dec.append(int(i,2)*2)
    enc_text = ""
    for i in liste_dec:
        if i>71:
            enc_text += alphabet[i%71]
        else:
            enc_text += alphabet[i]
    return enc_text
print(xor(xor("<previous pass>","<first part>"),"<second part>")[::-1])
