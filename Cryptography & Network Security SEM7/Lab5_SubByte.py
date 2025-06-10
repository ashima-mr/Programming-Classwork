def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def galois_multiplicative_inverse(byte): #0x11b is multiplicative inverse of a byte in GF(2^8)
    if byte == 0:
        return 0  # Inverse of 0 is defined as 0
    gcd, x, _ = extended_gcd(byte, 0x11b)  #find the irreducible polynomial
    if gcd != 1:
        raise ValueError("Inverse does not exist for byte {}".format(byte))
    return x % 256

def byte_to_matrix(byte):
    return [(byte >> i) & 1 for i in range(8)]

def matrix_to_byte(matrix):
    return sum([bit << i for i, bit in enumerate(matrix)])

def subbyte(byte):
    a = galois_multiplicative_inverse(byte)
    b = byte_to_matrix(a)
    
    c = [0] * 8
    for i in range(8):
        c[i] = b[i] ^ b[(i + 4) % 8] ^ b[(i + 5) % 8] ^ b[(i + 6) % 8] ^ b[(i + 7) % 8]
    
    d = [0] * 8
    for i in range(8):
        d[i] = c[i] ^ byte_to_matrix(0x63)[i] 
    
    return matrix_to_byte(d)

def subbytes(state):
    for r in range(4):
        for c in range(4):
            state[r][c] = subbyte(state[r][c])
    return state

state = [
    [0x32, 0x88, 0x31, 0xe0],
    [0x43, 0x5a, 0x31, 0x37],
    [0xf6, 0x30, 0x98, 0x07],
    [0xa8, 0x8d, 0xa2, 0x34]
]

new_state = subbytes(state)
print("Transformed State:")
for row in new_state:
    print([hex(byte) for byte in row])
