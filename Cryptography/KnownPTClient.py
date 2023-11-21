import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))

    known_plaintext = input("Enter known plaintext: ")
    client_socket.sendall(known_plaintext.encode())

    ciphertext = input("Enter ciphertext: ")
    client_socket.sendall(ciphertext.encode())

    response = client_socket.recv(1024).decode()
    print("Server response:", response)

if __name__ == "__main__":
    main()
