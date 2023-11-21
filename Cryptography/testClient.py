# shift cipher
import socket
import numpy as np
def fillChar(msg,keySize):
    while(len(msg)%keySize!=0):
        msg+='x'
    return msg

def encrypt(msg, key):
    msg = fillChar(msg,len(key))
    # print(msg)
    ciphertext = ""
    for i in range(0,len(msg),len(key)):
        block = msg[i:i+len(key)]
        block = np.array([ord(ch)-ord('a') for ch in block])
        block = block.reshape(len(key),-1)
        result_matrix = (key @ block)%26
        ciphertext += "".join([chr(ch+ord('a')) for ch in result_matrix.flat])
    return ciphertext
host = "127.0.0.1"
port = 9003
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))

plaintext = input("Enter Plaintext : ")
keySize = int(input("Enter Key Size : "))
key = []
for i in range(keySize):
    temp = []
    for j in range(keySize):
        temp.append(int(input()))
    key.append(temp)
keyData = "\n".join(" ".join(map(str,row)) for row in key)

ciphertext = encrypt(plaintext,key)
print(f"Encrypted Text : {ciphertext}")
socket.send(ciphertext.encode())
socket.send(keyData.encode())
