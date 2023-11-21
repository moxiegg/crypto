import socket

def vigenere_decrypt(ciphertext, key):
    decrypted_message = ""
    key_idx = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)].upper()) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_idx += 1
        else:
            decrypted_char = char
        decrypted_message += decrypted_char

    return decrypted_message

def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server listening on {}:{}".format(host, port))

    client_socket, client_address = server_socket.accept()
    print("Connected by:", client_address)

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        encrypted_message, key = data.split(';')
        decrypted_message = vigenere_decrypt(encrypted_message, key)
        print(f"Decrypted Message: {decrypted_message}")
        client_socket.send(decrypted_message.encode())

    client_socket.close()

if __name__ == "__main__":
    main()
