def mix_columns(state):
    for c in range(4):  # Iterate over each column
        mix_column(state[c])

def mix_column(col):
    # Copy the column to a temporary variable
    t = col[:] 
    
    col[0] = gf_multiply(0x02, t[0]) ^ gf_multiply(0x03, t[1]) ^ t[2] ^ t[3]
    col[1] = t[0] ^ gf_multiply(0x02, t[1]) ^ gf_multiply(0x03, t[2]) ^ t[3]
    col[2] = t[0] ^ t[1] ^ gf_multiply(0x02, t[2]) ^ gf_multiply(0x03, t[3])
    col[3] = gf_multiply(0x03, t[0]) ^ t[1] ^ t[2] ^ gf_multiply(0x02, t[3])

def gf_multiply(x, y):
    result = 0
    for _ in range(8):
        if (y & 1) != 0:  # If the least significant bit is set
            result ^= x
        # Carry out the multiplication in GF(2^8)
        carry = x & 0x80  # Check if the highest bit is set
        x <<= 1           # Shift x left by 1
        if carry != 0:    # If there was a carry
            x ^= 0x1b     # XOR with the irreducible polynomial
        y >>= 1           # Shift y right by 1
    return result

def print_state(state):
    for row in state:
        print(row)

state = [
    [0x01, 0x02, 0x03, 0x04],
    [0x11, 0x12, 0x13, 0x14],
    [0x21, 0x22, 0x23, 0x24],
    [0x31, 0x32, 0x33, 0x34],
]

print("Before MixColumns:")
print_state(state)

mix_columns(state)

print("\nAfter MixColumns:")
print_state(state)
