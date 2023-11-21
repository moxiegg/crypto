# import socket
# import numpy as np

# def fillChar(msg,keySize):
#     while(len(msg)%keySize!=0):
#         msg+='x'
#     return msg

# # def multiply(key,temp):
# #     ans=[]
# #     for i in key:
# #         x=0
# #         for j in range(len(key)):
# #             x=x+i[j]*temp[j]
# #         ans.append(x % 26)
# #     return ans


# # def encrypt(msg,key):
# #     keySize=len(key)
# #     msg = fillChar(msg,keySize)
# #     ciphertext=""
# #     for i in range(len(msg)//keySize):
# #         temp=[]
# #         for ch in range(i*keySize,i*keySize+keySize):
# #             temp.append(ord(msg[ch])-ord('a'))
# #         ans=multiply(key,temp)
# #         for num in ans:
# #             ciphertext += (chr)(ord('a')+num)
# #     return ciphertext

# def encrypt(msg,key):
#     key_matrix = np.array(key)
#     msg_matrix = np.array([ord(ch)-ord('a') for ch in msg])
#     msg_matrix = msg_matrix.reshape(-1,len(key))

#     result_matrix = (msg_matrix @ key_matrix) % 26

#     ciphertext = "".join([chr(ord('a')+num) for num in result_matrix.flat])
#     return ciphertext

# plaintext = input("Enter Plaintext:")
# keySize = int(input("Enter Key Size:"))
# key = []
# for i in range(keySize):
#     temp = []
#     for j in range(keySize):
#         ele = int(input())
#         temp.append(ele)
#     print(temp)
#     key.append(temp)
# print(key)
# print(encrypt(plaintext,key))
# # plaintext=fillChar(plaintext,keySize)
# # print(plaintext)


import socket
import numpy as np

def fillChar(msg, keySize):
    while len(msg) % keySize != 0:
        msg += 'x'
    return msg

#works only for lowercase characters
def encrypt(msg, key):
    keySize = len(key)
    msg = fillChar(msg, keySize)

    # Create NumPy arrays for key and message
    key_matrix = np.array(key)
    ciphertext = ""
    print(key_matrix)
    for i in range(0,len(msg),keySize):
        block = msg[i:i+keySize]
        block_matrix = np.array([ord(ch)-ord('a') for ch in block])
        block_matrix = block_matrix.reshape(keySize,-1)
        print(block_matrix)
        # Multiply the matrices efficiently
        result_matrix = (key_matrix @ block_matrix) % 26
        ciphertext += "".join([chr(ch+ord('a')) for ch in result_matrix.flat])

    # Convert the result back to characters
    return ciphertext


plaintext = input("Enter Plaintext:")
keySize = int(input("Enter Key Size:"))
key = []

print("Enter the key matrix:")
for i in range(keySize):
    temp = []
    for j in range(keySize):
        ele = int(input())
        temp.append(ele)
    key.append(temp)

host = "127.0.0.1"
port = 5842
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))
data = encrypt(plaintext, key)
client_socket.send(data.encode())
print("Message Sent:", data)
matrix_str = "\n".join([" ".join(map(str, row)) for row in key])
client_socket.send(matrix_str.encode())
