import math
import random
 
p = 3
q = 7
n = p*q
phi = (p-1)*(q-1)
 
while True:
    e = random.randint(2, phi - 1)
    if math.gcd(e, phi) == 1:
        break 

def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

gcd, x, y = extended_euclidean(e, phi)
d = x % phi
 
print(p, q, n, e, d)
 
msg = 11
C = pow(msg, e) % n
print(f'Encrypted message: {C}')
 
M = pow(C, d) % n
 
print(f'Decrypted message: {M}')   