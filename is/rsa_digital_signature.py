from sha import sha1
from rsa import extended_euclidean

p = 61  
q = 53  
n = p * q 
phi = (p - 1) * (q - 1)  
e = 17  


def mod_inverse(e, phi):
    gcd, x, y = extended_euclidean(e, phi)
    return x % phi

d = mod_inverse(e, phi) 



def rsa_signature(message):
    digest = sha1(message)
    print(len(str(digest)))
    digital_signature = pow(digest, d, n) 
    return digital_signature


message = "1011111000101"
signature = rsa_signature(message)
print("Digital Signature:", signature)