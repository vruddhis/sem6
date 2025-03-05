import socket
import random 
import math

host = '127.0.0.1'
port = 10000

ss=socket.socket()
ss.bind((host, port))
ss.listen()

print("Connection established")
conn, addr = ss.accept()


print("Receiving p ")
p = conn.recv(1024)
p = int(p.decode())
print(p)
print("Receiving g ")
g = conn.recv(1024)
g = int(g.decode())

b = random.randint(1, 10)
B = int(math.pow(g, b) % p)

print("Receiving A ")
A = conn.recv(1024)
A = int(A.decode())


print("Sending B ", B)
conn.send(str(B).encode())

s = math.pow(A, b) % p

print("Shared secret is ", s)

ss.close()