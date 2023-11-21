import socket

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def encrypt(msg,e,n):
    e = int(e)
    n = int(n)
    msg = int(msg)
    temp = pow(msg,e)
    temp = temp % n
    return temp

host = "127.0.0.1"
port = 9003
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))

msg = int(input("Enter Message : "))

print("Receiving Server's Public Key....")
server_public_key = socket.recv(1024).decode().split(" ")
e = server_public_key[0]
n = server_public_key[1]
print(f"Server's Public Key : <{e},{n}>")
msg = encrypt(msg,e,n)
print(f"Encrypted Message : {msg}")
socket.send(str(msg).encode())

