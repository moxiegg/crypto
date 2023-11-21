import socket


def floorMod(a, b):
    return ((a % b) + b) % b


def decrypt(msg, a, b):
    a_inv = pow(a, -1, 26)
    plaintext = ""
    for ch in msg:
        if ch.islower():
            plaintext += (chr)(
                floorMod(a_inv * (ord(ch) - ord("a") - b), 26) + ord("a")
            )
        elif ch.isupper():
            plaintext += (chr)(
                floorMod(a_inv * (ord(ch) - ord("A") - b), 26) + ord("A")
            )
        else:
            plaintext += ch

    return plaintext


host = "127.0.0.1"
port = 9003
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()
client_socket, client_addr = server_socket.accept()
print(f"Connection from {client_addr}")
while True:
    msg = client_socket.recv(1024).decode()
    [data, a, b] = msg.split(" ")
    a = int(a)
    b = int(b)
    print(f"Received Message:{data}")
    print(f"Decrypted Message:{decrypt(data,a,b)}")
