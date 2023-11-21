import socket
import numpy as np

def matrix_inverse_mod26(matrix):
    det = int(np.round(np.linalg.det(matrix)))
    inv_det = pow(det, -1, 26)
    #det * inv gives the adjoint matrix 
    #inv_det * (det * inv) mod 26 gives us the inverse of key matrix in modular arithmetic 
    adj = np.round(inv_det * np.linalg.inv(matrix) * det) % 26
    return adj.astype(int)

def decrypt(msg, key):
    keySize = len(key)

    # Create NumPy arrays for key and message
    key_matrix = np.array(key)
    key_matrix = matrix_inverse_mod26(key)
    plaintext = ""
    for i in range(0,len(msg),keySize):
        block = msg[i:i+keySize]
        block_matrix = np.array([ord(ch)-ord('a') for ch in block])
        block_matrix = block_matrix.reshape(keySize,-1)
        # Multiply the matrices efficiently
        result_matrix = (key_matrix @ block_matrix) % 26
        plaintext += "".join([chr(ch+ord('a')) for ch in result_matrix.flat])

    # Convert the result back to characters
    return plaintext



host = "127.0.0.1"
port = 5842
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((host,port))
socket.listen()
client_socket,addr = socket.accept()
msg = client_socket.recv(1024).decode()
print("Received Message:",msg)
matrix_str = client_socket.recv(1024).decode()

# Split the string into rows and parse it into a matrix
key = [list(map(int, row.split())) for row in matrix_str.split("\n")]
print(decrypt(msg,key))


