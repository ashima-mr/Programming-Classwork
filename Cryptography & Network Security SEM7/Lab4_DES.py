IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

IP_INV = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

S_BOXES = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 9, 5, 0, 14, 12]],
    
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 7, 2, 12, 14]],
    
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 8, 15, 10, 3, 9, 6, 0],
     [9, 7, 0, 6, 3, 14, 5, 10, 15, 1, 13, 12, 11, 8, 2, 4],
     [2, 13, 8, 4, 6, 15, 11, 1, 10, 9, 3, 5, 12, 7, 0, 14]],
    
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 7, 3, 1, 13, 11, 6, 10, 0, 4],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 6, 8, 3, 9, 7, 5, 2, 15, 10, 14, 0],
     [3, 6, 12, 5, 15, 10, 9, 0, 8, 13, 1, 14, 7, 11, 8, 13]],

    [[13, 2, 8, 14, 15, 0, 3, 12, 9, 7, 5, 10, 11, 6, 1, 4],
     [1, 15, 11, 8, 10, 5, 12, 9, 7, 2, 3, 14, 13, 0, 6, 4],
     [10, 2, 7, 15, 12, 9, 1, 5, 14, 0, 8, 11, 4, 13, 3, 6],
     [7, 12, 2, 10, 4, 13, 14, 1, 11, 8, 3, 15, 6, 0, 9, 5]]
]

P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# Key schedule constants
PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

SHIFT_TABLE = [
    1, 1, 2, 2, 2, 2, 1, 2,
    2, 2, 1, 2, 2, 2, 1, 2
]

def permute(bits, table):
    return [bits[i - 1] for i in table]

def shift_left(bits, shifts):
    return bits[shifts:] + bits[:shifts]

def generate_subkeys(key):
    key56 = permute(key, PC1)
    C = key56[:28]
    D = key56[28:]
    
    subkeys = []
    for round in range(16):
        shifts = SHIFT_TABLE[round]
        C = shift_left(C, shifts)
        D = shift_left(D, shifts)
        combined_key = C + D
        subkey = permute(combined_key, PC2)
        subkeys.append(subkey)
    
    return subkeys

def permute(block, table):
    return [block[i - 1] for i in table]

def xor(block1, block2):
    return [b1 ^ b2 for b1, b2 in zip(block1, block2)]

def sbox_substitution(expanded_block):
    substituted_block = []
    for i in range(8):
        sbox = S_BOXES[i]
        block_segment = expanded_block[i * 6:(i + 1) * 6]
        row = 2 * block_segment[0] + block_segment[5]
        col = 8 * block_segment[1] + 4 * block_segment[2] + 2 * block_segment[3] + block_segment[4]
        value = sbox[row][col]
        substituted_block.extend([(value >> (3 - j)) & 1 for j in range(4)])
    return substituted_block

def f_function(right_block, round_key):
    expanded_block = permute(right_block, E)
    xor_result = xor(expanded_block, round_key)
    substituted_block = sbox_substitution(xor_result)
    return permute(substituted_block, P)

def mixer(left_block, right_block, round_key):
    t1 = right_block.copy()
    t2 = f_function(t1, round_key)
    t3 = xor(left_block, t2)
    right_block[:] = t3
    left_block[:] = t1

def swapper(left_block, right_block):
    left_block[:], right_block[:] = right_block, left_block

def des_round(plain_block, subkeys):
    ip_block = permute(plain_block, IP)
    left_block = ip_block[:32]
    right_block = ip_block[32:]
    
    for round_key in subkeys:
        mixer(left_block, right_block, round_key)
        swapper(left_block, right_block)
    
    combined_block = left_block + right_block
    cipher_block = permute(combined_block, IP_INV)
    
    return cipher_block


plain_block = [1] * 64  # 64-bit plaintext block 
original_key = [
    0, 1, 0, 0, 0, 1, 1, 0,
    0, 1, 0, 0, 0, 1, 1, 0,
    1, 1, 0, 0, 0, 1, 0, 1,
    1, 0, 0, 0, 1, 0, 1, 1,
    0, 1, 1, 0, 1, 1, 0, 1,
    1, 0, 1, 0, 1, 1, 1, 0,
    1, 1, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 0, 1, 1,
]

subkeys = generate_subkeys(original_key)

cipher_block = des_round(plain_block, subkeys)

print("Cipher Block:", cipher_block)
