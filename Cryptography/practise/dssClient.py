import socket
host = "127.0.0.1"
port = 5842
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((host,port))

p = int(input("Prime Number : "))
q = int(input(f"Prime Divisor of ({p}-1) : "))
h = int(input("h : "))
g = pow(h, (p - 1) // q, p)
x = int(input(f"Random Integer <{q} : "))
y = pow(g, x, p)
k = int(input(f"Per message Secret Key <{q}: "))
#signing
r = pow(g,k,p)
r = r % q
k_inv = pow(k,-1,q)
hash_val = int(input("Enter Hash[H(M)] : "))
s = (k_inv*(hash_val+x*r)) % q

print(f"Signature = ({r},{s})")

#sending p,q,s,hash_val,r,g,y
msg = " ".join(map(str,[p,q,s,hash_val,r,g,y]))
socket.send(msg.encode())
