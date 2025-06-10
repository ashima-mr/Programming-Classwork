def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2, x1 = x1, x
        d, y1 = y1, y

    if temp_phi == 1:
        return d + phi

def encrypt(plaintext, public_key):
    e, n = public_key
    encrypted_blocks = [(ord(char) ** e) % n for char in plaintext]
    return encrypted_blocks

def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_blocks = [(char ** d) % n for char in ciphertext]
    decrypted_text = ''.join([chr(block) for block in decrypted_blocks])
    return decrypted_text

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))


p = int(input())
q = int(input())
public_key, private_key = generate_keypair(p, q)

plaintext = input()
ciphertext = encrypt(plaintext, public_key)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt(ciphertext, private_key)
print("Decrypted text:", decrypted_text)
