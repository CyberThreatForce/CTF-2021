from hashlib import sha256
import base64
import time
import random
import string



class Block:
    def __init__(self,numero_block, data, block=None):
        self.num_block = 0 if not block else block.num_block + 1
        self.nonce = 0
        self.data = data
        self.hash_precedent = None if not block else block.hash
        self.hash = self._hashage()
        self.bloc_precedent = None if not block else block
        self.valide = False
        self.time = 0
    def _hashage(self):
        if self.hash_precedent:
            chaine = str(self.num_block)+str(self.nonce)+self.data+self.hash_precedent
            chaine = chaine[::-1]
        else:
            chaine = str(self.num_block)+str(self.nonce)+self.data
            chaine = chaine[::-1]
        self.hash = base64.b64encode(bytes(chaine, 'utf-8')).decode("utf-8")
        return self.hash
    def __str__(self):
        table = '\n'.join([f"\nInfos for Block number {self.num_block}",f"- Last hash : {self.hash_precedent}",f"- Hash      : {self.hash}",f"- Valid     : {self.valide}",f"- Nonce     : {self.nonce}",f"- Time      : {self.time}\n"])
        return table
    def minage(self):
        start = time.time()
        print('\033[94m'+f"\n[*] Mining Block {self.num_block}"+'\033[0m')
        self.hash = ""
        while self.hash[-2:]!="==":
            self._hashage()
            self.nonce += 1
        self.nonce -= 1
        stop = time.time()
        self.time = stop-start
        self.valide = True
        return '\033[92mValid Hash Found :' + str(self.hash)+str(self.nonce)+'\033[0m'
    def chaine_valide(self):
        block = self
        while block.bloc_precedent!= None:
            #print(f'Checking : {block}')
            if not block.valide:
                return False
            block = block.bloc_precedent
        return True
    
    def check_mine(self):
        print('\033[93m'+"\n[+] Auto Mine:"+'\033[0m')
        liste_blocs = []
        if not self.chaine_valide():
            block = self
            while block.valide != False:
                liste_blocs.append(block)
                block = block.bloc_precedent
            liste_blocs.append(block)
            for i in liste_blocs[::-1]:
                i.hash_precedent = i.bloc_precedent.hash
                i._hashage()
                i.minage()
                
            return "Done"
        else:
            return True

    def auto_mine(self):
        while self.check_mine()!=True:
            pass

def launch2():
    if __name__ == "__main__":
        global password
        password = random.choice(["bere198524130571","strawberry","12345678910","sg745255644","hellokate2","cipro16081608","barton315","barto@123","snookie#3","snoop-dog95","SCORPIO14","skillz89","skillz89"])
        hash = sha256(bytes(password,"utf-8")).hexdigest()
        block = Block(1, hash)
        block.minage()

        alphabet = string.ascii_lowercase
        blocks = []
        blocks.append(block)
        for i in range(4):
            chaine = "".join(random.choice(alphabet) for j in range(100))
            blocks.append(Block(i,chaine,blocks[-1]))
        
        blocks[-1].auto_mine()

        with open("out.txt","w") as file:
            file.write(str(blocks[-1]))
        return blocks[-1]



        #print('\033[92m'+"\n[+] Hashs Verified"+'\033[0m') if blocks[-1].chaine_valide() else print('\033[91m'+"\n[+] Invalid Hashs"+'\033[0m')


def launch1():
    import socket
    from multiprocessing import Process
    import time
    import random
    import base64
    import os

    list_of_ip = {}
    if __name__=="__main__":

        #proc = Process(target=start_receiver)
        #proc.start()
        print("Server ok")
        #ip=""
        ip = "0.0.0.0"
        port=1234
        bufferSize  = 1024




        socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        compteur = 0
        socket1.bind((ip, port))
        while True:
            global password
            if compteur%30 == 0:
                launch2()
            if compteur>100000:
                compteur = 0
            help = "code <code> - to enter the code \nhelp        - Display this message\nblock        - Display the current block\n"
            with open("out.txt","r") as file:
                data = file.read()
            message,addr = socket1.recvfrom(bufferSize)
            message = message.decode("utf-8").replace('\n',"")
            print(message)
            if message.upper() == "HELP":
                to_send = help+"\n"
            elif message.upper() == "BLOCK":
                to_send = data+"\n"
            elif "CODE" in message.upper():
                try:
                    code = message.split(" ")[1]
                except IndexError:
                    code = ""
                if code == password:
                    to_send = "CYBERTF{M1nInG_B1Tc01n!}\n"
                    compteur += 1
                else:
                    to_send = "Wrong Password \n"
            else:
                to_send = "Enter help to get help\n"
            socket1.sendto(bytes(to_send,"utf-8"), addr)


        proc.join()
launch1()
