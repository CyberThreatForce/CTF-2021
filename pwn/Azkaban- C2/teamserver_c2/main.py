import socket
import random

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

serverSocket.bind(('', 9050));
serverSocket.listen();

while (True):
    (clientConnected, clientAddress) = serverSocket.accept();

    #print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]));


    pinFromClient = clientConnected.recv(1024)
    print(pinFromClient.decode());

    n1 = random.randint(0, 1000)

    n2 = random.randint(0, 1000)


    res = str(n1 + n2)
    clientConnected.send(("[*]BruteForce - Protection\nSend result of " + str(n1) + " + " + str(n2) + "\n").encode());

    bruteforceProctectionFromClient = clientConnected.recv(1024)

    if pinFromClient.decode() == "4785":
        print("IP :%s \nPIN : CORRECT" % (clientAddress[0]));


    if bruteforceProctectionFromClient.decode() == res:
        print("OK")

    #print(bruteforceProctectionFromClient.decode())
    #Si le pin est bon, sa connecte
    if pinFromClient.decode() == "4785" and bruteforceProctectionFromClient.decode() == res:



        clientConnected.send("""Welcome to Azkaban - C2 SERVER\n""".encode());
        clientConnected.send("""1)Implants connectées\n""".encode());
        clientConnected.send("""2)Dump creds\n3)Credit\n""".encode());

        (clientConnected, clientAddress) = serverSocket.accept();
        dataFromClient2 = clientConnected.recv(1024)

        if dataFromClient2.decode() == "1":
            clientConnected.send("Liste des implants connectés :\n ".encode());
            clientConnected.send("_______________________________________\n".encode());
            clientConnected.send("| ID      | Hostname | IP              |\n".encode());
            clientConnected.send("_______________________________________\n".encode());
            clientConnected.send("| DbpRha  | PC012    | 192.168.15.124  |\n ".encode());
            clientConnected.send("_______________________________________\n".encode());

        elif dataFromClient2.decode() == "2":
            clientConnected.send("Dump des pass/hash\n".encode());
            clientConnected.send("____________________________________________________________\n".encode());
            clientConnected.send("| Pass           | Username | Site                          |\n".encode());
            clientConnected.send("____________________________________________________________\n".encode());
            clientConnected.send("| .W$vjDEmV7YR/  | s3rgue1   | dontexist.onion              |\n ".encode());
            clientConnected.send("____________________________________________________________\n".encode());
            clientConnected.send("| 4709F798A8CFBDC870420453276E0B8E  | Administrator   | .  |\n ".encode());
            clientConnected.send("___________________________________________________________\n".encode());
            clientConnected.send("| kuBtV9T}a]YP} | s3llcr3d1tc4rd   | dontexist.onion       |\n ".encode());
            clientConnected.send("___________________________________________________________\n".encode());


        elif dataFromClient2.decode() == "3":
            clientConnected.send("Liste des implants connectés : ".encode());
        else:
            clientConnected.send("ERREUR - CHOIX INCONNUS ".encode());



    else:
        clientConnected.send("[-] Connection refused to Azkaban C2 \n".encode());


    #clientConnected.send("Hello Client!".encode());