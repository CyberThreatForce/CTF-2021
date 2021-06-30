import random
import math


def encrypt(message,n,e):
    phrase_deci_enc = []
    for i in message:
        phrase_deci_enc.append(str((ord(i)**e)%n))
    return " ".join(phrase_deci_enc)

def decrypt(message,d,n):
    chaine = ""
    for i in message.split(" "):
        chaine+=str(chr((int(i)**d)%n))
    return chaine


p=int(input("P:"))
q=int(input("q :"))
n=p*q
r=(p-1)*(q-1)
print(f"n={n}")
print(f"r={r}")
liste = []
for i in range(r*10):
    if i%r == 1:
        liste.append(i)
liste_good=[]
for i in liste:
    if i%r == 1:
        liste_good.append(i)
factorizables={}
for i in liste_good:
    for j in range(2,i):
        if i%j == 0:
            factorizables[i]=f"{j} {int(i/j)}"
            break
to_keep = {}
for i in factorizables:
    if (int(factorizables[i].split(" ")[0])*int(factorizables[i].split(" ")[1]))%r == 1:
        if math.gcd(int(factorizables[i].split(" ")[0]),n)==1 and math.gcd(int(factorizables[i].split(" ")[1]),n)==1:
            to_keep[i]=factorizables[i]
key = random.choice(list(to_keep.keys()))

e = int(to_keep[key].split(" ")[0])
d = int(to_keep[key].split(" ")[1])

print(f"Public Key ({e},{n})")

print(f"Private Key ({d},{n})")

cipher = encrypt("",n,e)
print(f"encrypted message : {cipher}")
print(f"decrypted message : {decrypt(cipher,d,n)}")
