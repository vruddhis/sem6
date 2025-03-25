import socket
import random
import math
import sys
import time

host = '127.0.0.1'
port = 10000

cs=socket.socket()
cs.connect((host, port))

print("Connection established")

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

def findGenerator(p):
    r = set(range(1, p))
    
    for i in range(1, p):
        gen = set()
        for x in r:
            gen.add(pow(i,x,p))
        if gen == r:
            return i


g = findGenerator(p)

print("Sending p ", p)
cs.send(str(p).encode())

time.sleep(2)
print("Sending g ", g)
cs.send(str(g).encode())

a = random.randint(1, 10)
A = int(math.pow(g, a) % p)
time.sleep(2)
print("Sending A ", A)
cs.send(str(A).encode())
time.sleep(2)
print("Receiving B ")
B = cs.recv(1024)
B = int(B.decode())


s = math.pow(B, a) % p

print("Shared secret is ", s)

