import socket
import math
def fillMatrix(msg,key):
    d=0
    cols = len(key)
    rows = math.ceil(len(msg)/len(key))
    arr=[['' for i in range(cols)]
         for j in range(rows)]
    order = [key.index(i) for i in sorted(key)]
    # arranging the cipher message into matrix
    # to get the same matrix as in encryption
    for i in order:
        for j in range(rows):
            arr[j][i]=msg[d]
            d+=1
    return arr

def decrypt(msg,key):
    matrix = fillMatrix(msg,key)
    plaintext = ""
    rows = math.ceil(len(msg)/len(key))
    for i in range(rows):
        for j in range(len(key)):
            plaintext+=matrix[i][j]
    return plaintext

host = "127.0.0.1"
port = 5842
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((host,port))
socket.listen()
client_socket,addr = socket.accept()
print(f"Connection from {addr}")
msg = client_socket.recv(1024).decode()
key = client_socket.recv(1024).decode()
print(f"Received : {msg} \n Key : {key}")
print(decrypt(msg,key))