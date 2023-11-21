def mod_inv(a):
    try:
        a_inv=pow(a,-1,26)
    except:
        return -1
    else:
        return a_inv

def encrypt(msg, a, b):
    ciphertext = ""
    for ch in msg:
        if ch.islower():
            ciphertext += chr(((ord(ch)-ord('a'))*a + b) % 26 + ord('a'))
        elif ch.isupper():
            ciphertext += chr(((ord(ch)-ord('A'))*a + b) % 26 + ord('A'))
        else:
            ciphertext += ch
    return ciphertext

def floorMod(a,b):
    return ((a%b)+b)%b

def decrypt(msg,a,b):
    a_inv=mod_inv(a)
    plaintext = ""
    for ch in msg:
        if ch.islower():
            plaintext += chr(floorMod(a_inv*(ord(ch)-ord('a')-b),26)+ord('a'))
        elif ch.isupper():
            plaintext += chr(floorMod(a_inv*(ord(ch)-ord('A')-b),26)+ord('A'))
        else:
            plaintext += ch
    return plaintext

plaintext = input("Enter Plaintext : ")
a = int(input("Enter a : "))
b = int(input("Enter b : "))
if mod_inv(a)==-1:
    print(f"No Modular Inverse exists for {a}")
else:
    print("---------------Brute Force Attack-------------")
    msg = encrypt(plaintext,a,b)
    print(f"Ciphertext : {msg}")
    a_val = [1,3,5,7,9,11,15,17,19,21,23,25]
    for a in a_val:
        for b in range(26):
            print(f"a : {a}\tb : {b}\t|Message : {decrypt(msg,a,b)}")
# print(decrypt(msg,a,b))
print("\n-----------------Known Ciphertext and Plaintext Attack----------------")
plain = input("Enter Known Plaintext(atleast 2 char) : ")
cipher = input("Enter Corresponding Ciphertext(same length as plaintext) : ")
flag = False
for a in a_val:
    for b in range(26):
        if encrypt(plain,a,b)==cipher:
            print("Found the Key Pair :")
            print(f"a : {a}\t b : {b}")
            flag = True
            break
if not flag:
    print("Impossible Pairs of Plaintext and Ciphertext")