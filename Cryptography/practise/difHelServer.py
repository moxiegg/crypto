import socket

def is_primitive(n,p):
    residues = set()
    for i in range(1,p):
        residue = pow(n,i,p)
        residues.add(residue)
    return len(residues)==p-1

def primitive_root(p):
    for i in range(p):
        if(is_primitive(i,p)):
            return i
        
host = "127.0.0.1"
port = 9003
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((host,port))
socket.listen()
client_socket,addr = socket.accept()
print(f"Connection from {addr}")

prime = int(input("Enter Prime(same as client) : "))
root = primitive_root(prime)
print(f"Sending Prime : {prime} and Primitive Root : {root} to client")
msg = str(prime)+" "+str(root)
client_socket.send(msg.encode())
b = int(input("Enter b : "))

y = pow(root,b,prime)

print(f"y : {y}")
print("Sending y to client...")
client_socket.send(str(y).encode())
print("\nReceiving x from client...")
x = int(client_socket.recv(1024).decode())
print(f"x : {x}")

K = pow(x,b,prime)
print(f"Server's secret key : {K}")


