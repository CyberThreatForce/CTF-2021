#!/usr/bin/python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
import sys

FLAG = "CYBERTF{WTF_It's_u$eless_in_real_w0rld}"+"\x00"
KEY = open("data.key","rb").read()
def ajust(x):
    while len(x)%16!=0:
        x+="\x00"
    return x
text = input("input: ")
text += FLAG
cipher = AES.new(KEY,AES.MODE_ECB)

#on utilise le fd de stdout et on ecrit bytes a bytes le result
#print(cipher.encrypt(ajust(text).encode()))
os.write(sys.stdout.fileno(), cipher.encrypt(pad(text.encode(), 16)))
