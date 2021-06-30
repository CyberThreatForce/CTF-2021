from Crypto.PublicKey import RSA

def decrypt(message,d,n):
    chaine = ""
    message = str(message)
    for i in message.split(" "):
        chaine+=str(chr((int(i)**d)%n))
    return chaine

with open("key.pem","r") as file:
    pubkey = file.read()

pub_key = RSA.importKey(pubkey)

print(pub_key.e)
print(pub_key.n)

e = pub_key.e
d = 0
n = pub_key.n
prime = 347
message_part = 194813

for i in range(100000):
    if n%prime == 0:
        r = ((n/prime)-1)*(prime-1)
        if (e*i)%r == 1:
            print(i,decrypt(message_part,i,n))
