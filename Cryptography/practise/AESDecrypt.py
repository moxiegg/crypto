import numpy as np

r_con = (
    0x00000000, 0x01000000, 0x02000000, 0x04000000, 0x08000000, 0x10000000, 0x20000000, 0x40000000, 0x80000000, 0x1B000000, 0x36000000
)

aes_sbox = [
    [int('63', 16), int('7c', 16), int('77', 16), int('7b', 16), int('f2', 16), int('6b', 16), int('6f', 16), int('c5', 16), int(
        '30', 16), int('01', 16), int('67', 16), int('2b', 16), int('fe', 16), int('d7', 16), int('ab', 16), int('76', 16)],
    [int('ca', 16), int('82', 16), int('c9', 16), int('7d', 16), int('fa', 16), int('59', 16), int('47', 16), int('f0', 16), int(
        'ad', 16), int('d4', 16), int('a2', 16), int('af', 16), int('9c', 16), int('a4', 16), int('72', 16), int('c0', 16)],
    [int('b7', 16), int('fd', 16), int('93', 16), int('26', 16), int('36', 16), int('3f', 16), int('f7', 16), int('cc', 16), int(
        '34', 16), int('a5', 16), int('e5', 16), int('f1', 16), int('71', 16), int('d8', 16), int('31', 16), int('15', 16)],
    [int('04', 16), int('c7', 16), int('23', 16), int('c3', 16), int('18', 16), int('96', 16), int('05', 16), int('9a', 16), int(
        '07', 16), int('12', 16), int('80', 16), int('e2', 16), int('eb', 16), int('27', 16), int('b2', 16), int('75', 16)],
    [int('09', 16), int('83', 16), int('2c', 16), int('1a', 16), int('1b', 16), int('6e', 16), int('5a', 16), int('a0', 16), int(
        '52', 16), int('3b', 16), int('d6', 16), int('b3', 16), int('29', 16), int('e3', 16), int('2f', 16), int('84', 16)],
    [int('53', 16), int('d1', 16), int('00', 16), int('ed', 16), int('20', 16), int('fc', 16), int('b1', 16), int('5b', 16), int(
        '6a', 16), int('cb', 16), int('be', 16), int('39', 16), int('4a', 16), int('4c', 16), int('58', 16), int('cf', 16)],
    [int('d0', 16), int('ef', 16), int('aa', 16), int('fb', 16), int('43', 16), int('4d', 16), int('33', 16), int('85', 16), int(
        '45', 16), int('f9', 16), int('02', 16), int('7f', 16), int('50', 16), int('3c', 16), int('9f', 16), int('a8', 16)],
    [int('51', 16), int('a3', 16), int('40', 16), int('8f', 16), int('92', 16), int('9d', 16), int('38', 16), int('f5', 16), int(
        'bc', 16), int('b6', 16), int('da', 16), int('21', 16), int('10', 16), int('ff', 16), int('f3', 16), int('d2', 16)],
    [int('cd', 16), int('0c', 16), int('13', 16), int('ec', 16), int('5f', 16), int('97', 16), int('44', 16), int('17', 16), int(
        'c4', 16), int('a7', 16), int('7e', 16), int('3d', 16), int('64', 16), int('5d', 16), int('19', 16), int('73', 16)],
    [int('60', 16), int('81', 16), int('4f', 16), int('dc', 16), int('22', 16), int('2a', 16), int('90', 16), int('88', 16), int(
        '46', 16), int('ee', 16), int('b8', 16), int('14', 16), int('de', 16), int('5e', 16), int('0b', 16), int('db', 16)],
    [int('e0', 16), int('32', 16), int('3a', 16), int('0a', 16), int('49', 16), int('06', 16), int('24', 16), int('5c', 16), int(
        'c2', 16), int('d3', 16), int('ac', 16), int('62', 16), int('91', 16), int('95', 16), int('e4', 16), int('79', 16)],
    [int('e7', 16), int('c8', 16), int('37', 16), int('6d', 16), int('8d', 16), int('d5', 16), int('4e', 16), int('a9', 16), int(
        '6c', 16), int('56', 16), int('f4', 16), int('ea', 16), int('65', 16), int('7a', 16), int('ae', 16), int('08', 16)],
    [int('ba', 16), int('78', 16), int('25', 16), int('2e', 16), int('1c', 16), int('a6', 16), int('b4', 16), int('c6', 16), int(
        'e8', 16), int('dd', 16), int('74', 16), int('1f', 16), int('4b', 16), int('bd', 16), int('8b', 16), int('8a', 16)],
    [int('70', 16), int('3e', 16), int('b5', 16), int('66', 16), int('48', 16), int('03', 16), int('f6', 16), int('0e', 16), int(
        '61', 16), int('35', 16), int('57', 16), int('b9', 16), int('86', 16), int('c1', 16), int('1d', 16), int('9e', 16)],
    [int('e1', 16), int('f8', 16), int('98', 16), int('11', 16), int('69', 16), int('d9', 16), int('8e', 16), int('94', 16), int(
        '9b', 16), int('1e', 16), int('87', 16), int('e9', 16), int('ce', 16), int('55', 16), int('28', 16), int('df', 16)],
    [int('8c', 16), int('a1', 16), int('89', 16), int('0d', 16), int('bf', 16), int('e6', 16), int('42', 16), int('68', 16), int(
        '41', 16), int('99', 16), int('2d', 16), int('0f', 16), int('b0', 16), int('54', 16), int('bb', 16), int('16', 16)]
]

inv_aes_sbox = [
    [int('52', 16), int('09', 16), int('6a', 16), int('d5', 16), int('30', 16), int('36', 16), int('a5', 16), int('38', 16), int(
        'bf', 16), int('40', 16), int('a3', 16), int('9e', 16), int('81', 16), int('f3', 16), int('d7', 16), int('fb', 16)],
    [int('7c', 16), int('e3', 16), int('39', 16), int('82', 16), int('9b', 16), int('2f', 16), int('ff', 16), int('87', 16), int(
        '34', 16), int('8e', 16), int('43', 16), int('44', 16), int('c4', 16), int('de', 16), int('e9', 16), int('cb', 16)],
    [int('54', 16), int('7b', 16), int('94', 16), int('32', 16), int('a6', 16), int('c2', 16), int('23', 16), int('3d', 16), int(
        'ee', 16), int('4c', 16), int('95', 16), int('0b', 16), int('42', 16), int('fa', 16), int('c3', 16), int('4e', 16)],
    [int('08', 16), int('2e', 16), int('a1', 16), int('66', 16), int('28', 16), int('d9', 16), int('24', 16), int('b2', 16), int(
        '76', 16), int('5b', 16), int('a2', 16), int('49', 16), int('6d', 16), int('8b', 16), int('d1', 16), int('25', 16)],
    [int('72', 16), int('f8', 16), int('f6', 16), int('64', 16), int('86', 16), int('68', 16), int('98', 16), int('16', 16), int(
        'd4', 16), int('a4', 16), int('5c', 16), int('cc', 16), int('5d', 16), int('65', 16), int('b6', 16), int('92', 16)],
    [int('6c', 16), int('70', 16), int('48', 16), int('50', 16), int('fd', 16), int('ed', 16), int('b9', 16), int('da', 16), int(
        '5e', 16), int('15', 16), int('46', 16), int('57', 16), int('a7', 16), int('8d', 16), int('9d', 16), int('84', 16)],
    [int('90', 16), int('d8', 16), int('ab', 16), int('00', 16), int('8c', 16), int('bc', 16), int('d3', 16), int('0a', 16), int(
        'f7', 16), int('e4', 16), int('58', 16), int('05', 16), int('b8', 16), int('b3', 16), int('45', 16), int('06', 16)],
    [int('d0', 16), int('2c', 16), int('1e', 16), int('8f', 16), int('ca', 16), int('3f', 16), int('0f', 16), int('02', 16), int(
        'c1', 16), int('af', 16), int('bd', 16), int('03', 16), int('01', 16), int('13', 16), int('8a', 16), int('6b', 16)],
    [int('3a', 16), int('91', 16), int('11', 16), int('41', 16), int('4f', 16), int('67', 16), int('dc', 16), int('ea', 16), int(
        '97', 16), int('f2', 16), int('cf', 16), int('ce', 16), int('f0', 16), int('b4', 16), int('e6', 16), int('73', 16)],
    [int('96', 16), int('ac', 16), int('74', 16), int('22', 16), int('e7', 16), int('ad', 16), int('35', 16), int('85', 16), int(
        'e2', 16), int('f9', 16), int('37', 16), int('e8', 16), int('1c', 16), int('75', 16), int('df', 16), int('6e', 16)],
    [int('47', 16), int('f1', 16), int('1a', 16), int('71', 16), int('1d', 16), int('29', 16), int('c5', 16), int('89', 16), int(
        '6f', 16), int('b7', 16), int('62', 16), int('0e', 16), int('aa', 16), int('18', 16), int('be', 16), int('1b', 16)],
    [int('fc', 16), int('56', 16), int('3e', 16), int('4b', 16), int('c6', 16), int('d2', 16), int('79', 16), int('20', 16), int(
        '9a', 16), int('db', 16), int('c0', 16), int('fe', 16), int('78', 16), int('cd', 16), int('5a', 16), int('f4', 16)],
    [int('1f', 16), int('dd', 16), int('a8', 16), int('33', 16), int('88', 16), int('07', 16), int('c7', 16), int('31', 16), int(
        'b1', 16), int('12', 16), int('10', 16), int('59', 16), int('27', 16), int('80', 16), int('ec', 16), int('5f', 16)],
    [int('60', 16), int('51', 16), int('7f', 16), int('a9', 16), int('19', 16), int('b5', 16), int('4a', 16), int('0d', 16), int(
        '2d', 16), int('e5', 16), int('7a', 16), int('9f', 16), int('93', 16), int('c9', 16), int('9c', 16), int('ef', 16)],
    [int('a0', 16), int('e0', 16), int('3b', 16), int('4d', 16), int('ae', 16), int('2a', 16), int('f5', 16), int('b0', 16), int(
        'c8', 16), int('eb', 16), int('bb', 16), int('3c', 16), int('83', 16), int('53', 16), int('99', 16), int('61', 16)],
    [int('17', 16), int('2b', 16), int('04', 16), int('7e', 16), int('ba', 16), int('77', 16), int('d6', 16), int('26', 16), int(
        'e1', 16), int('69', 16), int('14', 16), int('63', 16), int('55', 16), int('21', 16), int('0c', 16), int('7d', 16)]
]

const_mat = [
    [0x02, 0x03, 0x01, 0x01],[0x01, 0x02, 0x03, 0x01],[0x01, 0x01, 0x02, 0x03],[0x03, 0x01, 0x01, 0x02]
]

inv_const_mat = [
    [0x0E, 0x0B, 0x0D, 0x09], [0x09, 0x0E, 0x0B, 0x0D], [0x0D, 0x09, 0x0E, 0x0B], [0x0B, 0x0D, 0x09, 0x0E]
]

def str_to_hex(str_in):
    hex_out = ""
    for ch in str_in:
        hex_out += format(ord(ch), 'x')
    return hex_out

def hex_to_str(hex_in):
    return ''.join([chr(int(hex_in[i : i + 2], 16)) for i in range(0, len(hex_in), 2)])

def rot_word(str_in):
    return str_in[2:] + str_in[:2]

def sub_word(str_in):
    hex_vals = [str_in[i : i + 2] for i in range(0, len(str_in), 2)]
    str_sub = ""
    for val in hex_vals:
        row = int(val[0], 16)
        col = int(val[1], 16)
        str_sub += f'{aes_sbox[row][col]:02X}'
    return str_sub

def xor(a, b):
    return hex(a ^ b)[2:].zfill(8)

def generate_keys(key):
    key = str_to_hex(key)

    # to be commented out
    # key = "2475A2B33475568831E2120013AA5487".lower()

    key_zero = [key[i:i+8] for i in range(0, len(key), 8)] # [w0 w1 w2 w3]
    keys = []
    keys.append(key_zero)
    
    for i in range(1, 11):
        key_ith_round = []
        for j in range(4):
            prev_key = keys[-1]
            if j == 0:
                wi_minus_1, wi_minus_4 = prev_key[-1], prev_key[0]
                t = xor(int(sub_word(rot_word(wi_minus_1)), 16), r_con[i])
                key_ith_round.append(xor(int(t, 16), int(wi_minus_4, 16)))
            else:
                wi_minus_1, wi_minus_4 = key_ith_round[-1], prev_key[j]
                key_ith_round.append(xor(int(wi_minus_1, 16), int(wi_minus_4, 16)))
        keys.append(key_ith_round)

    return keys

def add_round_key(state_mat, key):
    key_mat = np.array([[k[i : i + 2] for k in key] for i in range(0, len(key[0]), 2)])
    key_mat = key_mat.reshape(4, 4)
    key_mat = np.array([[int(ele, 16) for ele in row] for row in key_mat])
    state_mat = np.array([[int(ele, 16) for ele in row] for row in state_mat])
    res = key_mat ^ state_mat
    res = [[hex(ele)[2:].zfill(2) for ele in row] for row in res]
    return res

def sub_block(state, inv=False):
    new_state = state
    i = 0
    for word in state:
        j = 0
        for byt in word:
            row = int(byt[0], 16)
            col = int(byt[1], 16)
            new_state[i][j] = f'{(aes_sbox[row][col] if not inv else inv_aes_sbox[row][col]):02X}'
            j += 1
        i += 1
    return new_state

def shift_block(state, dir):
    new_state = np.empty_like(state)

    shifts = [0, 1, 2, 3]

    for row in range(4):
        new_state[row] = np.roll(state[row], -shifts[row] if dir == "left" else shifts[row])

    return new_state

def multiply_by_2(v):
    s = v << 1
    s &= 0xff
    if (v & 128) != 0:
        s = s ^ 0x1b
    return s

def multiply_by_3(v):
    return multiply_by_2(v) ^ v

def multiply_by_9(v):
    return multiply_by_2(multiply_by_2(multiply_by_2(v))) ^ v

def multiply_by_11(v):
    return multiply_by_2(multiply_by_2(multiply_by_2(v))) ^ multiply_by_2(v) ^ v

def multiply_by_13(v):
    return multiply_by_2(multiply_by_2(multiply_by_2(v))) ^ multiply_by_2(multiply_by_2(v)) ^ v

def multiply_by_14(v):
    return multiply_by_2(multiply_by_2(multiply_by_2(v))) ^ multiply_by_2(multiply_by_2(v)) ^ multiply_by_2(v)

def inverse_mix_column(column):
    r = [
        multiply_by_14(column[0]) ^ multiply_by_11(column[1]) ^ multiply_by_13(column[2]) ^ multiply_by_9(column[3]),
        multiply_by_9(column[0]) ^ multiply_by_14(column[1]) ^ multiply_by_11(column[2]) ^ multiply_by_13(column[3]),
        multiply_by_13(column[0]) ^ multiply_by_9(column[1]) ^ multiply_by_14(column[2]) ^ multiply_by_11(column[3]),
        multiply_by_11(column[0]) ^ multiply_by_13(column[1]) ^ multiply_by_9(column[2]) ^ multiply_by_14(column[3]),
    ]
    return r

def mix_column(column):
    r = [
        multiply_by_2(column[0]) ^ multiply_by_3(
            column[1]) ^ column[2] ^ column[3],
        multiply_by_2(column[1]) ^ multiply_by_3(
            column[2]) ^ column[3] ^ column[0],
        multiply_by_2(column[2]) ^ multiply_by_3(
            column[3]) ^ column[0] ^ column[1],
        multiply_by_2(column[3]) ^ multiply_by_3(
            column[0]) ^ column[1] ^ column[2],
    ]
    return r

def mix_columns(grid, inv=False):
    new_grid = [[], [], [], []]
    for i in range(4):
        col = [grid[j][i] for j in range(4)]
        col = mix_column(col) if not inv else inverse_mix_column(col)
        for k in range(4):
            new_grid[k].append(col[k])
    return new_grid

def encrypt(pt, keys):
    pt_hex = str_to_hex(pt)
    print(pt_hex)
    pt_matrix = np.array([pt_hex[i : i + 2] for i in range(0, len(pt_hex), 2)])
    pt_matrix = pt_matrix.reshape(4, 4)
    pt_matrix = pt_matrix.transpose()

    new_state = add_round_key(pt_matrix, keys[0])

    for i in range(1, 11):

        # subbytes
        new_state = sub_block(new_state)
        
        # shift row
        new_state = shift_block(new_state, "left")

        if i != 10:
            # mix columns
            new_state = np.array([[int(ele, 16) for ele in row] for row in new_state])
            new_state = mix_columns(new_state)
            new_state = [[hex(ele)[2:].zfill(2) for ele in row] for row in new_state]
     
        # add round key
        new_state = add_round_key(new_state, keys[i])
        print(f'{i} {new_state}')

    new_state = np.transpose(new_state)
    ct_hex = ""        
    for i in new_state:
        for j in i:
            ct_hex += j
    return ct_hex

def decrypt(ct_hex, keys):
    ct_matrix = np.array([ct_hex[i: i + 2] for i in range(0, len(ct_hex), 2)])
    ct_matrix = ct_matrix.reshape(4, 4)
    ct_matrix = ct_matrix.transpose()
    new_state = ct_matrix

    for i in range(0, 10):
        # add round key
        new_state = add_round_key(new_state, keys[i])     

        # inverse mix columns
        if i != 0:
            new_state = np.array([[int(ele, 16) for ele in row] for row in new_state])
            new_state = mix_columns(new_state, inv=True)
            new_state = [[hex(ele)[2:].zfill(2) for ele in row] for row in new_state]   

        # inverse shift (shift right)
        new_state = shift_block(new_state, dir='right')

        # inverse sub bytes
        new_state = sub_block(new_state, inv=True)

        print(f'{i} {new_state}')
    
    new_state = add_round_key(new_state, keys[10])

    new_state = np.transpose(new_state)
    pt_hex = ""
    for row in new_state:
        for ele in row:
            pt_hex += ele

    return hex_to_str(pt_hex)

# key = input("Enter the key(16 chars): ")
# plain_text = input("Enter the plain text(16 chars): ")

# to be commented
# key = "abishekborn21nov"
# plain_text = "helloabihowareyu"
key = "Thats my Kung Fu"
plain_text = "Two One Nine Two"

keys = generate_keys(key)

cipher_text = encrypt(plain_text, keys)
print(cipher_text)

print()

keys.reverse()
print(decrypt(cipher_text, keys))