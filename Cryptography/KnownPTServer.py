import socket

def calculate_caesar_key(known_plaintext, ciphertext):
    shift = ord(ciphertext[0]) - ord(known_plaintext[0])
    if shift < 0:
        shift += 26  # Handling negative shifts
    return shift

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen()

    print("Server listening on port 12345...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Client connected: {client_address}")

        with client_socket:
            known_plaintext = client_socket.recv(1024).decode().strip()
            ciphertext = client_socket.recv(1024).decode().strip()

            key = calculate_caesar_key(known_plaintext, ciphertext)
            client_socket.sendall(f"The Caesar cipher key is: {key}\n".encode())

if __name__ == "__main__":
    main()
