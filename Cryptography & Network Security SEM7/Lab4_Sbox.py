# 4x16 S-box matrix
S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

def s_box_substitution(s_box, input_bits):
    # Extract row and column from 6-bit input: 1st and last bits give the row and remaining 4 bits give the column
    row = ((input_bits >> 5) & 0x01) * 2 + ((input_bits >> 0) & 0x01) # & 0x01 masks the input to extract the last bit alone
    column = (input_bits >> 1) & 0x0F

    return s_box[row][column]

input_bits = 0b110101
output = s_box_substitution(S1, input_bits)

print(f"Input (6-bit): {input_bits:06b}")
print(f"Substitution result (4-bit): {output:04b}")
