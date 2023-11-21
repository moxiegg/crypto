import socket

def encrypt(msg,key):
    ciphertext=""
    for ch in msg:
        if ch.islower():
            ciphertext+=(chr)(((ord(ch)-ord('a')+key)%26)+ord('a'))
        elif ch.isupper():
            ciphertext+=(chr)(((ord(ch)-ord('A')+key)%26)+ord('A'))
        else:
            ciphertext+=ch
    return ciphertext

host = "127.0.0.1"
port = 9003
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))
while True:
    pt=input("Enter PlainText:")
    key=int(input("Enter Key:"))
    data=encrypt(pt,key)
    print(f"Message Sent:{data}")
    client_socket.send(data.encode())
    client_socket.send(str(key).encode())
    print("--------------------------\n")
