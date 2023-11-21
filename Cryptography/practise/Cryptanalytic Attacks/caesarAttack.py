def floorMod(a,b):
    return ((a%b)+b)%b

def encrypt(msg, key):
    ciphertext = ""
    for ch in msg:
        if ch.islower():
            ciphertext += chr((ord(ch) - ord('a') + key)%26 + ord('a'))
        elif ch.isupper():
            ciphertext += chr((ord(ch) - ord('A') + key)%26 + ord('A'))
        else:
            ciphertext += ch
    return ciphertext

def decrypt(msg,key):
    plaintext = ""
    for ch in msg:
        if ch.islower():
            plaintext += chr(floorMod((ord(ch)-ord('a')-key),26) + ord('a'))
        elif ch.isupper():
            plaintext += chr(floorMod((ord(ch)-ord('A')-key),26) + ord('A'))
        else:
            plaintext += ch
    return plaintext

print("............Brute Force Attack.............")
plaintext = input("Enter Plaintext : ")
key = int(input("Enter Shift Value : "))
ciphertext = encrypt(plaintext,key)
print("\n Cipher Text:",ciphertext)
for i in range(26):
    print(f"Shift Value:{i}\t| Message:{decrypt(ciphertext,i)}")
print()
print("............Known Ciphertext and Plaintext.............")
plain = input("Enter Plaintext : ")
cipher = input("Enter Corresponding Ciphertext : ")
key = floorMod(ord(cipher[0])-ord(plain[0]),26)
print(f"Key is : {key}")
cipher = input("Ciphertext to be Decrypted : ")
print(f"Plaintext : {decrypt(cipher,key)}")