def modular_exponentiation(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if (exponent % 2) == 1:  # If exponent is odd
            result = (result * base) % mod
        exponent = exponent >> 1  # Divide exponent by 2
        base = (base * base) % mod
    return result


def alice_key_exchange(p, g):
    a = 6  
    A = modular_exponentiation(g, a, p)  # A = g^a mod p
    return A, a

def bob_key_exchange(p, g):
    b = 15  
    B = modular_exponentiation(g, b, p)  # B = g^b mod p
    return B, b

def shared_secret(partner_public_key, private_key, p):
    return modular_exponentiation(partner_public_key, private_key, p)

def main():
    p=23
    g= 5
    print(f"Prime (p): {p}, Generator (g): {g}")
    
    A, a = alice_key_exchange(p, g)
    print(f"Alice sends A: {A}")

    B, b = bob_key_exchange(p, g)
    print(f"Bob sends B: {B}")

    alice_shared_secret = shared_secret(B, a, p)
    bob_shared_secret = shared_secret(A, b, p)

    print(f"Alice's shared secret: {alice_shared_secret}")
    print(f"Bob's shared secret: {bob_shared_secret}")

if __name__ == "__main__":
    main()
