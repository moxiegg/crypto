import socket
import random

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print("Server listening on", server_ip, "port", server_port)

    client_socket, client_address = server_socket.accept()
    print("Connected by", client_address)

    while True:
        plaintext = client_socket.recv(1024).decode()
        if not plaintext:
            break
        
        shift = random.randint(1, 25)  # Generate a random shift value for each plaintext
        ciphertext = caesar_encrypt(plaintext, shift)
        print(f"Encrypted Message: {ciphertext}")
        client_socket.send(ciphertext.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
