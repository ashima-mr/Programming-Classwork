# Define the permutation and shifting tables
P10 = [
    3, 5, 2, 7, 4, 10, 1, 9, 8, 6
]

P8 = [
    6, 3, 7, 4, 8, 5, 10, 9
]

SHIFT_TABLE = [
    1, 2  # Number of left shifts for each key generation round
]

def permute(key, table):
    """ Permute key according to the given table """
    return [key[i - 1] for i in table]

def shift_left(bits, shifts):
    """ Shift bits left by a given number of positions """
    return bits[shifts:] + bits[:shifts]

def generate_subkeys(key):
    """ Generate 2 subkeys for S-DES from the original key """
    # Step 1: Apply P10 permutation
    key10 = permute(key, P10)
    
    # Step 2: Split key into two 5-bit halves
    C = key10[:5]
    D = key10[5:]
    
    # Generate two subkeys
    subkeys = []
    for i in range(2):
        # Step 3: Shift C and D
        shifts = SHIFT_TABLE[i]
        C = shift_left(C, shifts)
        D = shift_left(D, shifts)
        
        # Combine C and D
        combined_key = C + D
        
        # Step 4: Apply P8 permutation
        subkey = permute(combined_key, P8)
        subkeys.append(subkey)
    
    return subkeys

# Example key (10-bit)
original_key = [
    1, 0, 1, 1, 0, 0, 1, 1, 0, 0
]

# Generate the 2 subkeys
subkeys = generate_subkeys(original_key)

# Print the subkeys
for i, subkey in enumerate(subkeys):
    print(f"Subkey {i + 1}: {subkey}")
