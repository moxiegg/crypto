import math
import numpy as np
import itertools

def fillChar(msg, keySize):
    while len(msg) % keySize != 0:
        msg += 'x'
    return msg

#works only for lowercase characters
def encrypt(msg, key):
    keySize = int(math.sqrt(len(key)))
    msg = fillChar(msg, keySize)
    key_matrix = keytomatrix(key,keySize)

    ciphertext = ""
    for i in range(0,len(msg),keySize):
        block = msg[i:i+keySize]
        block_matrix = np.array([ ord(ch)-ord('a')  for ch in block] )
        block_matrix=block_matrix.reshape(keySize,-1)
        result_matrix=(key_matrix @ block_matrix)%26
        ciphertext += "".join([chr(ord('a') + num) for num in result_matrix.flat])
    return ciphertext

def keytomatrix(key, size):
    key_matrix = np.array([ord(ch) - ord('a') for ch in key])
    key_matrix = key_matrix.reshape(size, size)
    return key_matrix

def check(key, size):
    key_matrix = keytomatrix(key, size)
    d = int(np.round(np.linalg.det(key_matrix)))
    d = d % 26
    return not (d == 0 or d % 2 == 0 or d % 13 == 0)

def attack(plain_text, encrypted_text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key_size = int(input("Enter Key Size : "))
    word_length = key_size * key_size

    combinations = [''.join(combination) for combination in itertools.product(alphabet, repeat=word_length)]
    for word in combinations:
        if(check(word,key_size)):
            if(encrypt(plain_text,word)==encrypted_text):
                print("Key is : ")
                print(f"{word}\n{keytomatrix(word,2)}")
                break

plaintext = (input("Enter Plaintext : "))
ciphertext = (input("Enter Ciphertext : "))
attack(plaintext,ciphertext)