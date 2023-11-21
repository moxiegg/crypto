import socket

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def decrypt(msg,d,n):
    d = int(d)
    msg = int(msg)
    n = int(n)
    temp = pow(msg,d)
    temp = temp % n
    return temp

host = "127.0.0.1"
port = 9003
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
socket.listen()
client_socket,addr = socket.accept()

p = int(input("Enter p : "))
q = int(input("Enter q : "))
n = p * q
phi = (p - 1) * (q - 1)
e = 2

while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

d=pow(e,-1,phi)

print(f"\nServer :\nPublic Key : <{e},{n}>\nPrivate Key : <{d},{n}>")
print("\nSending public key to Client.....\n")
msg = str(e)+" "+str(n)
client_socket.send(msg.encode())
msg = client_socket.recv(1024).decode()
print(f"Received Message : {msg}")
print(f"Decrypted Message : {decrypt(msg,d,n)}")

