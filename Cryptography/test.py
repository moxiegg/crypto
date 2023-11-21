Sbox = (
    0x63,
    0x7C,
    0x77,
    0x7B,
    0xF2,
    0x6B,
    0x6F,
    0xC5,
    0x30,
    0x01,
    0x67,
    0x2B,
    0xFE,
    0xD7,
    0xAB,
    0x76,
    0xCA,
    0x82,
    0xC9,
    0x7D,
    0xFA,
    0x59,
    0x47,
    0xF0,
    0xAD,
    0xD4,
    0xA2,
    0xAF,
    0x9C,
    0xA4,
    0x72,
    0xC0,
    0xB7,
    0xFD,
    0x93,
    0x26,
    0x36,
    0x3F,
    0xF7,
    0xCC,
    0x34,
    0xA5,
    0xE5,
    0xF1,
    0x71,
    0xD8,
    0x31,
    0x15,
    0x04,
    0xC7,
    0x23,
    0xC3,
    0x18,
    0x96,
    0x05,
    0x9A,
    0x07,
    0x12,
    0x80,
    0xE2,
    0xEB,
    0x27,
    0xB2,
    0x75,
    0x09,
    0x83,
    0x2C,
    0x1A,
    0x1B,
    0x6E,
    0x5A,
    0xA0,
    0x52,
    0x3B,
    0xD6,
    0xB3,
    0x29,
    0xE3,
    0x2F,
    0x84,
    0x53,
    0xD1,
    0x00,
    0xED,
    0x20,
    0xFC,
    0xB1,
    0x5B,
    0x6A,
    0xCB,
    0xBE,
    0x39,
    0x4A,
    0x4C,
    0x58,
    0xCF,
    0xD0,
    0xEF,
    0xAA,
    0xFB,
    0x43,
    0x4D,
    0x33,
    0x85,
    0x45,
    0xF9,
    0x02,
    0x7F,
    0x50,
    0x3C,
    0x9F,
    0xA8,
    0x51,
    0xA3,
    0x40,
    0x8F,
    0x92,
    0x9D,
    0x38,
    0xF5,
    0xBC,
    0xB6,
    0xDA,
    0x21,
    0x10,
    0xFF,
    0xF3,
    0xD2,
    0xCD,
    0x0C,
    0x13,
    0xEC,
    0x5F,
    0x97,
    0x44,
    0x17,
    0xC4,
    0xA7,
    0x7E,
    0x3D,
    0x64,
    0x5D,
    0x19,
    0x73,
    0x60,
    0x81,
    0x4F,
    0xDC,
    0x22,
    0x2A,
    0x90,
    0x88,
    0x46,
    0xEE,
    0xB8,
    0x14,
    0xDE,
    0x5E,
    0x0B,
    0xDB,
    0xE0,
    0x32,
    0x3A,
    0x0A,
    0x49,
    0x06,
    0x24,
    0x5C,
    0xC2,
    0xD3,
    0xAC,
    0x62,
    0x91,
    0x95,
    0xE4,
    0x79,
    0xE7,
    0xC8,
    0x37,
    0x6D,
    0x8D,
    0xD5,
    0x4E,
    0xA9,
    0x6C,
    0x56,
    0xF4,
    0xEA,
    0x65,
    0x7A,
    0xAE,
    0x08,
    0xBA,
    0x78,
    0x25,
    0x2E,
    0x1C,
    0xA6,
    0xB4,
    0xC6,
    0xE8,
    0xDD,
    0x74,
    0x1F,
    0x4B,
    0xBD,
    0x8B,
    0x8A,
    0x70,
    0x3E,
    0xB5,
    0x66,
    0x48,
    0x03,
    0xF6,
    0x0E,
    0x61,
    0x35,
    0x57,
    0xB9,
    0x86,
    0xC1,
    0x1D,
    0x9E,
    0xE1,
    0xF8,
    0x98,
    0x11,
    0x69,
    0xD9,
    0x8E,
    0x94,
    0x9B,
    0x1E,
    0x87,
    0xE9,
    0xCE,
    0x55,
    0x28,
    0xDF,
    0x8C,
    0xA1,
    0x89,
    0x0D,
    0xBF,
    0xE6,
    0x42,
    0x68,
    0x41,
    0x99,
    0x2D,
    0x0F,
    0xB0,
    0x54,
    0xBB,
    0x16,
)

rcon = [[1, 0, 0, 0]]
for _ in range(1, 10):
    rcon.append([rcon[-1][0] * 2, 0, 0, 0])
    if rcon[-1][0] > 0x80:
        rcon[-1][0] ^= 0x11B


state = [
    [0x63, 0xEB, 0x9F, 0xA0],
    [0x2F, 0x93, 0x92, 0xC0],
    [0xAF, 0xC7, 0xAB, 0x30],
    [0xA2, 0x20, 0xCB, 0x2B],
]
key = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02],
]


def shift(row, n=1):
    row = row[n:] + row[:n]
    return row


def sub_byte(row):
    ans = []
    for i in row:
        ans.append(Sbox[i])
    return ans


def xor(row1, row2):
    ans = [row1[i] ^ row2[i] for i in range(4)]
    return ans


def g(word, round_number):
    ans = shift(word, 1)
    ans = sub_byte(ans)
    ans = xor(ans, rcon[round_number])
    return ans


def setKey(master_key):
    key = [int(hex(ord(ch)), 16) for ch in master_key]
    word = [[], [], [], []]
    word[0] = key[0:4]
    word[1] = key[4:8]
    word[2] = key[8:12]
    word[3] = key[12:16]
    round_key = []
    round_key.append([word[0], word[1], word[2], word[3]])
    for i in range(0, 10):
        temp = g(word[3], i)
        word[0] = xor(word[0], temp)
        word[1] = xor(word[1], word[0])
        word[2] = xor(word[2], word[1])
        word[3] = xor(word[3], word[2])
        round_key.append([word[0], word[1], word[2], word[3]])
    return round_key


def multiply_2(val):
    s = val << 1
    s &= 0xFF
    if (s & 128) != 0:
        s ^= 0x1B
    return s


def multiply_3(val):
    return multiply_2(val) ^ val


def mixColumn(column):
    r = [
        multiply_2(column[0]) ^ multiply_3(column[1]) ^ column[2] ^ column[3],
        multiply_2(column[1]) ^ multiply_3(column[2]) ^ column[0] ^ column[3],
        multiply_2(column[2]) ^ multiply_3(column[3]) ^ column[0] ^ column[1],
        multiply_2(column[3]) ^ multiply_3(column[0]) ^ column[1] ^ column[2],
    ]
    return r


def mixColumns(grid):
    new_grid = [[], [], [], []]
    for i in range(4):
        col = [grid[j][i] for j in range(4)]
        col = mixColumn(col)
        for i in range(4):
            new_grid[i].append(col[i])
    return new_grid


def addRoundKey(state, key):
    new_state = []
    for i in range(4):
        temp = []
        for j in range(4):
            temp.append(state[i][j] ^ key[i][j])
        new_state.append(temp)
    return new_state


def transpose(matrix):
    new_matrix = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_matrix[i][j] = matrix[j][i]
    return new_matrix


def matrix_to_hex(matrix):
    for i in matrix:
        for j in i:
            print(hex(j), end=" ")
        print()


def encryption(plaintext, key):
    key = setKey(key)
    plaintext = [int(hex(ord(ch)), 16) for ch in plaintext]
    state = []

    for i in range(0, 16, 4):
        state.append([ch for ch in plaintext[i : i + 4]])
    state = transpose(state)

    for i in range(len(key)):
        key[i] = transpose(key[i])
    # print(len(key))
    # round 0
    print(key)
    new_state = addRoundKey(state, key[0])
    print(new_state)
    for i in range(1, 2):
        for j in range(4):
            new_state[j] = sub_byte(new_state[j])
            new_state[j] = shift(new_state[j], j)
        if i != 10:
            new_state = mix_columns(new_state)
        new_state = addRoundKey(new_state, key[i])
        print()
        (matrix_to_hex(new_state))
        print()


plaintext = "Two One Nine Two"
key = "Thats my Kung Fu"
encryption(plaintext, key)
