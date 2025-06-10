def matrix_multiply(a, b):
    return [
        (a[0][0] * b[0] + a[0][1] * b[1]) % 26,
        (a[1][0] * b[0] + a[1][1] * b[1]) % 26
    ]

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def inverse_matrix(matrix):
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
    inv_det = mod_inverse(det, 26)
    if inv_det == 0:
        raise ValueError("Matrix is not invertible")
    return [
        [(matrix[1][1] * inv_det) % 26, (-matrix[0][1] * inv_det) % 26],
        [(-matrix[1][0] * inv_det) % 26, (matrix[0][0] * inv_det) % 26]
    ]

def hill_encrypt(plain_txt, key_matrix):
    plain_txt = plain_txt.upper().replace(' ', '')
    cipher_txt = ""
    
    for i in range(0, len(plain_txt), 2):
        vector = [ord(plain_txt[i]) - ord('A'), ord(plain_txt[i+1]) - ord('A')]
        encrypted_vector = matrix_multiply(key_matrix, vector)
        cipher_txt += chr(encrypted_vector[0] + ord('A')) + chr(encrypted_vector[1] + ord('A'))

    return cipher_txt

def hill_decrypt(cipher_txt, key_matrix):
    cipher_txt = cipher_txt.upper().replace(' ', '')
    plain_txt = ""
    inv_key_matrix = inverse_matrix(key_matrix)
    
    for i in range(0, len(cipher_txt), 2):
        vector = [ord(cipher_txt[i]) - ord('A'), ord(cipher_txt[i+1]) - ord('A')]
        decrypted_vector = matrix_multiply(inv_key_matrix, vector)
        plain_txt += chr(decrypted_vector[0] + ord('A')) + chr(decrypted_vector[1] + ord('A'))

    return plain_txt

key_matrix = [[3, 3],
            [2, 5]]

plain_txt = input("Enter plaintext: ")
cipher_txt = hill_encrypt(plain_txt, key_matrix)
print(f"Cipher text: {cipher_txt}")

decrypted_txt = hill_decrypt(cipher_txt, key_matrix)
print(f"Decrypted text: {decrypted_txt}")
