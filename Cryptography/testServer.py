# shift cipher
import socket
import numpy as np

def findInv(key):
    det = int(np.round(np.linalg.det(key)))
    det_inv = pow(det,-1,26)
    adj = np.round(det_inv * np.linalg.inv(key) * det)%26
    return adj.astype(int)

def decrypt(ciphertext,key):
    keySize = len(key)
    key = findInv(key)
    plaintext = ""
    for i in range(0,len(ciphertext),keySize):
        block = ciphertext[i:i+keySize]
        block = np.array([ord(ch) - ord('a') for ch in block])
        block = block.reshape(keySize,-1)
        result_matrix = (key @ block) % 26
        plaintext += "".join([chr(ch + ord('a')) for ch in result_matrix.flat])
    return plaintext

host = "127.0.0.1"
port = 9003
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
client_socket, addr = server.accept()
print(f"Connection from {addr}")
ct = client_socket.recv(1024).decode()
key = (client_socket.recv(1024).decode()).split("\n")
for i in range(len(key)):
    key[i] = key[i].split(" ")
    key[i] = list(map(int,key[i]))
print(f"CT : {ct}")
print(key)
print(decrypt(ct, key))
