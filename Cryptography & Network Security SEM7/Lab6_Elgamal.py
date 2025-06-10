def modular_exponentiation(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if (exponent % 2) == 1:
            result = (result * base) % mod
        exponent = exponent >> 1
        base = (base * base) % mod
    return result

def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        quotient = a // m
        m, a = a % m, m
        x0, x1 = x1 - quotient * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keys():
    p = 23 
    a = 5 
    x = 6 
    y = modular_exponentiation(a, x, p) 
    return p, a, x, y

def encrypt(p, a, y, message):
    k = 15  
    K = modular_exponentiation(y, k, p)
    c1 = modular_exponentiation(a, k, p)
    c2 = (K*message) % p
    return c1, c2

def decrypt(p, x, ciphertext):
    c1, c2 = ciphertext
    K = modular_exponentiation(c1, x, p)
    K_inv = modular_inverse(K, p)
    message = (c2 * K_inv) % p
    return message

def main():
    p, a, x, y = generate_keys()
    print(f"Prime (p): {p}, Generator (a): {a}, Private Key (x): {x}, Public Key (y): {y}")
    
    message = 7 
    print(f"Original message: {message}")
    
    ciphertext = encrypt(p, a, y, message)
    print(f"Ciphertext: {ciphertext}")
    
    decrypted_message = decrypt(p, x, ciphertext)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
