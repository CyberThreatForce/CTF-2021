#!/usr/bin/python3
from hashlib import sha256
from os import system, execvp
import sys
import string

SECRET = "Ch3val0_S3cr3t3_M@st3r"

def check(val):
    return val.split(b"|")[1] == sha256(SECRET.encode() + val.split(b"|")[0]).hexdigest().encode()
def sanitize(val):
    out = ""
    for char in val:
        if char in string.printable:
            out += char
    return out

mesg = """
give me cmd|token
example: 
{}
{}
""".format(f"ls|{sha256(SECRET.encode() + b'ls').hexdigest()}", f"id|{sha256(SECRET.encode() + b'id').hexdigest()}")
try:
    print(mesg, flush=True)
    userInput = sys.stdin.buffer.readline()[:-1]
    if(check(userInput)):
        cmd =  userInput.split(b"|")[0].decode(errors="ignore")
        cmd = sanitize(cmd)
        system(cmd)
    else:
        print("Bad Token")
except Exception as E:
    print("WTF what are you doing")
