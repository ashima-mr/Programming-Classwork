# 56 bit
PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]

# 48 bits
PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

# Shifting table for each round
SHIFT_TABLE = [
    1, 1, 2, 2, 2, 2, 1, 2,
    2, 2, 1, 2, 2, 2, 1, 2
]

def permute(key, table):
    return [key[i - 1] for i in table] # i-1 bc indexing in permuation tables are 1-based indexing.

def shift_left(bits, shifts):
    
    ''' When performing a left shift we want to move each bit to the left and wrap the bits that go beyond the end back to the beginning.
     bits[shifts:] extracts the part of the list starting from index shifts to the end of the list i.e. the portion of the list that will be moved to the front after the shift. 
     bits[:shifts] extracts the part of the list from the start up to (but not including) index shifts i.e. the bit that wraps around after shifting'''
    
    return bits[shifts:] + bits[:shifts]

def generate_subkeys(key):
    #PC-1
    key56 = permute(key, PC1)
    
    #Splitting
    C = key56[:28]
    D = key56[28:]
    
    subkeys = []
    for round in range(16):
        #Shifting
        shifts = SHIFT_TABLE[round]
        C = shift_left(C, shifts)
        D = shift_left(D, shifts)

        combined_key = C + D
        
        #PC-2
        subkey = permute(combined_key, PC2)
        subkeys.append(subkey)
    
    return subkeys

# 64 bit
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

#generate 16 subkeys
subkeys = generate_subkeys(original_key)

for i, subkey in enumerate(subkeys):
    print(f"Round {i + 1} Subkey: {subkey}")
