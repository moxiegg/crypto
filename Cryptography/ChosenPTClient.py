import socket

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    plaintext = "my name is akshay"

    for shift in range(1, 26):
        print("Trying shift:", shift)
    
        client_socket.send(plaintext.encode())
        ciphertext = client_socket.recv(1024).decode()
        decrypted_plaintext = caesar_decrypt(ciphertext, shift)
        
        print("Shift:", shift, "| Plaintext:", plaintext, "| Decrypted:", decrypted_plaintext)
        
        if decrypted_plaintext != plaintext:
            continue
        else:
            print("Shift value found:", shift)
            break

    client_socket.close()

if __name__ == "__main__":
    main()
