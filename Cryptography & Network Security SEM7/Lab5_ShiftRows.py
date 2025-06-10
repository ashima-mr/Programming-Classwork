def shift_rows(state):
    for r in range(1, 4):  # Rows 1 to 3
        shift_row(state[r], r)

def shift_row(row, n):
    # Copy the row to a temporary variable
    t = row[:]  # Make a copy of the row
    for c in range(4):  # Columns 0 to 3
        # Shift the row by n positions
        row[c] = t[(c - n) % 4]

def print_state(state):
    for row in state:
        print(row)

state = [
    [0x01, 0x02, 0x03, 0x04],
    [0x11, 0x12, 0x13, 0x14],
    [0x21, 0x22, 0x23, 0x24],
    [0x31, 0x32, 0x33, 0x34],
]

print("Before ShiftRows:")
print_state(state)

shift_rows(state)

print("\nAfter ShiftRows:")
print_state(state)
