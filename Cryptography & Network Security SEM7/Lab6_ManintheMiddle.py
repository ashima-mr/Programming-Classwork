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

class MITMAttack:
    def __init__(self):
        self.eve_private_key = 10 

    def intercept(self, public_key):
        # Eve generates her own public key
        e_public_key = modular_exponentiation(5, self.eve_private_key, 23)
        print(f"Eve intercepts public key: {public_key} and sends her own: {e_public_key}")
        return e_public_key

    def compute_shared_secret(self, intercepted_public_key):
        return modular_exponentiation(intercepted_public_key, self.eve_private_key, 23)

def main_mitm():
    p=23
    g= 5
    print(f"Prime (p): {p}, Generator (g): {g}")

    alice = alice_key_exchange(p, g)
    print(f"Alice sends A: {alice[0]}")

    mitm = MITMAttack()
    intercepted_A = mitm.intercept(alice[0])

    bob = bob_key_exchange(p, g)
    print(f"Bob sends B: {bob[0]}")

    intercepted_B = mitm.intercept(bob[0])

    alice_shared_secret = shared_secret(intercepted_B, alice[1], p)
    bob_shared_secret = mitm.compute_shared_secret(intercepted_A)

    print(f"Alice's shared secret with Eve's interception: {alice_shared_secret}")
    print(f"Eve's shared secret with Bob: {bob_shared_secret}")

if __name__ == "__main__":
    main_mitm()
