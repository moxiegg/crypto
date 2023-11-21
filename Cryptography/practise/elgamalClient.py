import socket 

host = "127.0.0.1"
port = 9003
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

prime = int(input("Prime : "))
root = int(input("Primitive Root : "))
x = int(input("Enter x : "))
y = pow(root,x,prime)

socket.connect((host,port))
socket.send(str(y).encode())

msg = socket.recv(1024).decode().split(" ")

c1 = int(msg[0])
c2 = int(msg[1])

K = pow(c1,x,prime)
K_inv = pow(K,-1,prime)
plain = (c2 * K_inv) % prime
print(f"Received text form server : {plain}")