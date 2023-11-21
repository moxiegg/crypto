import socket 
def fillMatrix(msg,key):
    matrix=[]
    for i in range(0,len(msg),len(key)):
        temp = [ch for ch in msg[i:i+len(key)]]
        matrix.append(temp)
    # Fill the empty spaces
    while(len(matrix[-1])!=len(key)):
        matrix[-1].append("_")
    return matrix

def encrypt(msg,key):
    matrix = fillMatrix(msg,key)
    sort_key = sorted(key)
    ciphertext = ""
    for i in sort_key:
        # gets the index of the given character i from the actual key
        col = key.index(i)
        for j in range(len(matrix)):
            ciphertext+=matrix[j][col]
    return ciphertext

host = "127.0.0.1"
port = 5842
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))

plaintext = input("Enter Plaintext:")
key = input("Enter key as alphabet:")

msg=encrypt(plaintext,key)
print(f"Message Sent:{msg}")

client_socket.send(msg.encode())
client_socket.send(key.encode())