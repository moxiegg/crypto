import socket

def floorMod(a,b):
    return (((a%b)+b)%b)
def decrypt(msg,key):
    plaintext = ""
    for ch in msg:
        if ch.islower():
            plaintext += (chr)(floorMod((ord(ch)-ord('a')-key),26)+ord('a'))
        elif ch.isupper():
            plaintext += (chr)(floorMod((ord(ch)-ord('A')-key),26)+ord('A'))
        else:
            plaintext+=ch
    return plaintext

host = '127.0.0.1'
port = 9003
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((host,port))
serverSocket.listen()
client_socket,client_address = serverSocket.accept()
print(f"Connection from {client_address}")
while True:
    data=client_socket.recv(1024).decode()
    key=int(client_socket.recv(1024).decode())
    print(f"Received Text:{data}")
    print(f"Decrypted Text:{decrypt(data,key)}")
    print("-------------------\n")