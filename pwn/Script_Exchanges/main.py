import socket
from multiprocessing import Process
import time
import random
import base64
import os

list_of_passwords = ["january77","jay1990","jenny1996","youwillneverknow","mustang16","moxita","november04","p@$$word","whatever"]



def start_receiver():
    pass


if __name__=="__main__":

    #proc = Process(target=start_receiver)
    #proc.start()
    print("Server ok")
    #ip=""
    ip = "127.0.0.1"
    port=1234
    bufferSize  = 1024




    socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    socket1.bind((ip, port))
    while True:
        with open("template.txt","r") as file:
            replace = random.choice(list_of_passwords)
            data = file.read().replace("%%replace%%",replace)
        to_send = base64.b64encode(data.encode("utf-8"))
        #print(replace)
        message,addr = socket1.recvfrom(bufferSize)
        socket1.settimeout(1.5)
        print(message.decode("utf-8"))
        socket1.sendto(to_send, addr)
        try:
            r = socket1.recvfrom(bufferSize)
            if r[0].decode("utf-8") == replace+"\n":
                socket1.sendto(b"FLAG", addr)
            else:
                print(r[0].decode("utf-8"))
        except:
            socket1.sendto(b"Too Slow", addr)
        socket1.settimeout(None)



    proc.join()
