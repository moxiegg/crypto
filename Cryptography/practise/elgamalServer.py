import socket
host = "127.0.0.1"
port = 9003

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((host,port))
socket.listen()
client_socket,addr = socket.accept()
print(f"Connection from {addr}")

prime = int(input("Prime (same as client) : "))
root = int(input("Primitive Root (same as client) : "))

print("Receiving client's public key.....")
y = int(client_socket.recv(1024).decode())
print(f"Client's Public Key : {y}")

k = int(input("k : "))

M = int(input("Enter Message : "))
c1 = pow(root,k,prime)
c2 = (pow(y,k) * M) % prime
print(f"Sending {c1} and {c2} to client....")
msg = str(c1) + " " + str(c2)
client_socket.send(msg.encode())
