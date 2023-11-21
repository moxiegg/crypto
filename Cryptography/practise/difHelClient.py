import socket

host = "127.0.0.1"
port = 9003
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((host,port))

msg = socket.recv(1024).decode().split(" ")
prime = int(msg[0])
root = int(msg[1])

print("Received From Server....")
print(f"Prime Number(P) : {prime}\nPrimitive Root(G) : {root}")

a = int(input("Enter a : "))
x = pow(root,a,prime)

print(f"x : {x}")
print("Sending x to server...")
socket.send(str(x).encode())
print("\nReceiving y from server...")
y = int(socket.recv(1024).decode())
print(f"y : {y}")

K = pow(y,a,prime)
print(f"Client's secret key : {K}")


