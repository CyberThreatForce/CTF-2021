from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

e = 17
n = 287663
d = int("67409",16)
k = int("1145953",16)
p = int("829",16)
q = int("347",16)
# Construct a `RSAobj` with only ( n, e ), thus with only PublicKey
rsaKey = RSA.construct( ( n, e ) )
pubKey = rsaKey.publickey()

# Export if needed
pubKeyPEM = rsaKey.exportKey()
print(pubKeyPEM.decode('ascii'))


'''pub_key = RSA.importKey()
print(pub_key.n)
print(pub_key.e)''' # get n and e from cert

