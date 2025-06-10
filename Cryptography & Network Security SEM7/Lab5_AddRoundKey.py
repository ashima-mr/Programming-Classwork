def add_round_key(state, round_key):
    for c in range(4):
        for r in range(4):
            # XOR the state byte with the corresponding round key byte
            state[r][c] ^= round_key[r][c]
    
    return state

def print_state(state):
    for row in state:
        print(row)

state = [
    [0x01, 0x02, 0x03, 0x04],
    [0x11, 0x12, 0x13, 0x14],
    [0x21, 0x22, 0x23, 0x24],
    [0x31, 0x32, 0x33, 0x34],
]

round_key = [
    [0x2b, 0x7e, 0x15, 0x16],
    [0x28, 0xae, 0xd2, 0xa6],
    [0xab, 0xf7, 0x97, 0x74],
    [0x00, 0x00, 0x00, 0x00]
]

print("Before AddRoundKey:")
print_state(state)

add_round_key(state, round_key)

print("\nAfter AddRoundKey:")
print_state(state)
