import socket


def encrypt(msg, a, b):
    ciphertext = ""
    for ch in msg:
        if ch.islower():
            ciphertext += (chr)((((ord(ch) - ord("a")) * a + b) % 26) + ord("a"))
        elif ch.isupper():
            ciphertext += (chr)((((ord(ch) - ord("A")) * a + b) % 26) + ord("A"))
        else:
            ciphertext += ch
    return ciphertext


host = "127.0.0.1"
port = 9003
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
while True:
    msg = input("Enter Plaintext:")
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    data = encrypt(msg, a, b)
    msg = data + " " + str(a) + " " + str(b)
    print(f"Message Sent:{msg}\n")
    client_socket.send(msg.encode())
# client_socket.send(str(a).encode())
# client_socket.send(str(b).encode())
