import socket

# S-box Table
# We have 8 different 4x16 matrices for each S box
# It converts 48 bits to 32 bits
# Each S box will get 6 bits and output will be 4 bits
s_box = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ],
]

# Round count: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# Bits shifted:1 1 2 2 2 2 2 2 1  2  2  2  2  2  2  1
# Number of bit shifts
shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Initial Permutation Table: (input of 64bit block size is pasesed: 64bit -> 64bit)
initial_perm = [
    58,
    50,
    42,
    34,
    26,
    18,
    10,
    2,
    60,
    52,
    44,
    36,
    28,
    20,
    12,
    4,
    62,
    54,
    46,
    38,
    30,
    22,
    14,
    6,
    64,
    56,
    48,
    40,
    32,
    24,
    16,
    8,
    57,
    49,
    41,
    33,
    25,
    17,
    9,
    1,
    59,
    51,
    43,
    35,
    27,
    19,
    11,
    3,
    61,
    53,
    45,
    37,
    29,
    21,
    13,
    5,
    63,
    55,
    47,
    39,
    31,
    23,
    15,
    7,
]

# Permuted choice 1: (key is passed: 64bit -> 56bit)
# That is bit position 8, 16, 24, 32, 40, 48, 56 and 64 are discarded from the key.
perm_cho_1 = [
    57,
    49,
    41,
    33,
    25,
    17,
    9,
    1,
    58,
    50,
    42,
    34,
    26,
    18,
    10,
    2,
    59,
    51,
    43,
    35,
    27,
    19,
    11,
    3,
    60,
    52,
    44,
    36,
    63,
    55,
    47,
    39,
    31,
    23,
    15,
    7,
    62,
    54,
    46,
    38,
    30,
    22,
    14,
    6,
    61,
    53,
    45,
    37,
    29,
    21,
    13,
    5,
    28,
    20,
    12,
    4,
]

# Permuted choice 2: (key is passed into it after applying
# left shift to both halves: 56bit -> 56bit)
perm_cho_2 = [
    14,
    17,
    11,
    24,
    1,
    5,
    3,
    28,
    15,
    6,
    21,
    10,
    23,
    19,
    12,
    4,
    26,
    8,
    16,
    7,
    27,
    20,
    13,
    2,
    41,
    52,
    31,
    37,
    47,
    55,
    30,
    40,
    51,
    45,
    33,
    48,
    44,
    49,
    39,
    56,
    34,
    53,
    46,
    42,
    50,
    36,
    29,
    32,
]

# Expansion permutation table
expan_perm = [
    32,
    1,
    2,
    3,
    4,
    5,
    4,
    5,
    6,
    7,
    8,
    9,
    8,
    9,
    10,
    11,
    12,
    13,
    12,
    13,
    14,
    15,
    16,
    17,
    16,
    17,
    18,
    19,
    20,
    21,
    20,
    21,
    22,
    23,
    24,
    25,
    24,
    25,
    26,
    27,
    28,
    29,
    28,
    29,
    30,
    31,
    32,
    1,
]

# Permutation table
perm_table = [
    16,
    7,
    20,
    21,
    29,
    12,
    28,
    17,
    1,
    15,
    23,
    26,
    5,
    18,
    31,
    10,
    2,
    8,
    24,
    14,
    32,
    27,
    3,
    9,
    19,
    13,
    30,
    6,
    22,
    11,
    4,
    25,
]

# Final Permutaion Table
final_perm = [
    40,
    8,
    48,
    16,
    56,
    24,
    64,
    32,
    39,
    7,
    47,
    15,
    55,
    23,
    63,
    31,
    38,
    6,
    46,
    14,
    54,
    22,
    62,
    30,
    37,
    5,
    45,
    13,
    53,
    21,
    61,
    29,
    36,
    4,
    44,
    12,
    52,
    20,
    60,
    28,
    35,
    3,
    43,
    11,
    51,
    19,
    59,
    27,
    34,
    2,
    42,
    10,
    50,
    18,
    58,
    26,
    33,
    1,
    41,
    9,
    49,
    17,
    57,
    25,
]


def hexa_to_bin(msg):
    mp = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    binary = ""
    for ch in msg:
        binary += mp[ch]
    return binary


def bin_to_hexa(msg):
    mp = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }
    hexa = ""
    for i in range(0, len(msg), 4):
        ch = msg[i] + msg[i + 1] + msg[i + 2] + msg[i + 3]
        hexa += mp[ch]
    return hexa


def bin_to_dec(msg):
    dec = 0
    i = 0
    while msg != 0:
        dig = msg % 10
        dec = dec + dig * pow(2, i)
        i += 1
        msg = msg // 10
    return dec


def dec_to_bin(msg):
    binary = bin(msg).replace("0b", "")
    if len(binary) % 4 != 0:
        counter = 4 - len(binary) % 4
        for i in range(counter):
            binary = "0" + binary
    return binary


def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans


def permute(msg, perm, no_bits):
    ans = ""
    for i in range(no_bits):
        ans = ans + msg[perm[i] - 1]
    return ans


def left_shift(msg, nth_shifts):
    s = ""
    for i in range(nth_shifts):
        for j in range(1, len(msg)):
            s = s + msg[j]
        s = s + msg[0]
        msg = s
        s = ""
    return msg

def encrypt(msg, key):
    msg = hexa_to_bin(msg)
    key = hexa_to_bin(key)
    msg = permute(msg, initial_perm, 64)
    key = permute(key, perm_cho_1, 56)

    # splitting the plaintext
    left = msg[0:32]
    right = msg[32:64]

    # splitting the key
    l = key[0:28]
    r = key[28:56]

    # generating the round keys
    key_after_pc2_bin = []
    key_after_pc2_hex = []

    for i in range(16):
        l = left_shift(l, shift_table[i])
        r = left_shift(r, shift_table[i])
        combined = l + r
        round_key = permute(combined, perm_cho_2, 48)
        key_after_pc2_bin.append(round_key)
        key_after_pc2_hex.append(bin_to_hexa(round_key))

    # 16 rounds of DES
    for i in range(16):
        right_expand = permute(right, expan_perm, 48)
        xor_x = xor(right_expand, key_after_pc2_bin[i])

        s_box_str = ""
        for j in range(8):
            row = int(xor_x[j * 6] + xor_x[j * 6 + 5])
            col = int(
                xor_x[j * 6 + 1]
                + xor_x[j * 6 + 2]
                + xor_x[j * 6 + 3]
                + xor_x[j * 6 + 4]
            )
            row = bin_to_dec(row)
            col = bin_to_dec(col)
            val = s_box[j][row][col]
            s_box_str += dec_to_bin(val)

        s_box_str = permute(s_box_str, perm_table, 32)
        result = xor(left, s_box_str)
        left = result

        if i != 15:
            left, right = right, left
        print(
            str(j + 1).zfill(2),
            "     ",
            bin_to_hexa(left),
            "      ",
            bin_to_hexa(right),
            "   ",
            key_after_pc2_hex[j],
        )

    # after 16 rounds of DES
    combined = left + right
    ciphertext = permute(combined, final_perm, 64)
    return ciphertext


print("Enter the message to be encrypted: ")
plain_text = input()

print("Enter the 64bit key for encryption: ")
key = input()

cipher_text = bin_to_hexa(encrypt(plain_text, key))
print("Cipher text is: ", cipher_text)

host = "127.0.0.1"
port = 5842
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((host,port))
msg = cipher_text + " " + key
socket.send(msg.encode())
# print(left_shift("1000",2))
# print(permute("1100", [2, 3, 4, 1], 4))
# print(xor("1000", "1100"))
# print(dec_to_bin(2))
# print(bin_to_dec(1000))
# print(bin_to_hexa("10001000"))
# print(hexa_to_bin("88"))
