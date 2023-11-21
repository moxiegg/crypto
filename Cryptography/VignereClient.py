import socket

def vigenere_encrypt(message, key):
    encrypted_message = ""
    key_idx = 0

    for char in message:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)].upper()) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_idx += 1
        else:
            encrypted_char = char
        encrypted_message += encrypted_char

    return encrypted_message

def main():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("Enter the message to encrypt: ")
    key = input("Enter the encryption key: ")

    encrypted_message = vigenere_encrypt(message, key)
    print("Encrypted message:", encrypted_message)
    data = encrypted_message + ';' + key
    client_socket.send(data.encode())

    decrypted_message = client_socket.recv(1024).decode()
    print("Decrypted message:", decrypted_message)

    client_socket.close()

if __name__ == "__main__":
    main()
