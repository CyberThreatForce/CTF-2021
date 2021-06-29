#!/usr/bin/python3
import os

value = os.popen("md5sum /home/ctf-cracked/flag.txt | cut -d ' ' -f 1")
if value == "8b098e9d5692641375f8da6d399edf98":
    print("All is clear")
else:
    print("Contact Administrator")
