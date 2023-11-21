#hill cipher
import numpy as np

def fillChar(msg,keySize):
    while(len(msg)%keySize!=0):
        msg+='X'
    return msg

def invKeyMatrix(matrix):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det,-1,26)
    adj = np.round(det_inv * np.linalg.inv(matrix) * det) % 26
    return adj.astype(int)

def encrypt(msg,key):
    keySize = int(len(key)**0.5)
    msg=fillChar(msg,keySize)
    # msgMatrix = np.array([ord(ch)-ord('A') for ch in msg])
    # msgMatrix = msgMatrix.reshape(keySize,-1)
    key = np.array([ord(ch)-ord('A') for ch in key])
    key = key.reshape(keySize,-1)
    ciphertext=""
    for i in range(0,len(msg),keySize):
        block = msg[i:i+keySize]
        blockMatrix = np.array([ord(ch)-ord('A') for ch in block])
        result = key@blockMatrix % 26
        ciphertext += "".join([chr(ele+ord('A')) for ele in result.flat])
    return ciphertext

def decrypt(msg,key):
    keySize = int(len(key)**0.5)
    msg=fillChar(msg,keySize)
    # msgMatrix = np.array([ord(ch)-ord('A') for ch in msg])
    # msgMatrix = msgMatrix.reshape(keySize,-1)
    key = np.array([ord(ch)-ord('A') for ch in key])
    key = key.reshape(keySize,-1)
    key = invKeyMatrix(key)
    ciphertext=""
    for i in range(0,len(msg),keySize):
        block = msg[i:i+keySize]
        blockMatrix = np.array([ord(ch)-ord('A') for ch in block])
        result = key@blockMatrix % 26
        ciphertext += "".join([chr(ele+ord('A')) for ele in result.flat])
    return ciphertext

key = "GYBNQKURP"
msg = "ACT"
ct=(encrypt(msg,key))
print(ct)
pt = decrypt(ct,key)
print(pt)
