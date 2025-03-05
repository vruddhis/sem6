import math
import random

def isPrime(n):
    prime_flag = 0
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

while True:
    p = random.randint(2, 100)
    if isPrime(p):
        break

while True:
    q = random.randint(2, 100)
    if isPrime(q):
        break

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
 
print("p, q, n, e, d", p, q, n, e, d)
 
m = int(input("Enter message (number):"))
C = pow(m, e) % n
print('Encrypted message:', C)
 
M = pow(C, d) % n
 
print('Decrypted message: ', M)   
