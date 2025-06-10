def encrypt(plain_txt, key):
    plain_txt = plain_txt.upper()
    cipher_txt = ""
    for char in plain_txt:
        if char.isalpha():
            shift = ord(char) + key
            if shift > ord('Z'):
                shift -= 26
            cipher_char = chr(shift)
            cipher_txt += cipher_char
        else:
            cipher_txt += char
    
    return cipher_txt

def decrypt(cipher_txt, key):
    cipher_txt = cipher_txt.upper()
    plain_txt = ""
    for char in cipher_txt:
        if char.isalpha():
            shift = ord(char) - key
            if shift < ord('A'):
                shift += 26
            plain_char = chr(shift)
            plain_txt += plain_char
        else:
            plain_txt += char
    
    return plain_txt

print("21BAI1830")
plain_txt = input("Enter plaintext: ")
key = int(input("Enter key: "))
cipher_txt = encrypt(plain_txt, key)
print(f"Cipher text: {cipher_txt}")

decrypted_txt = decrypt(cipher_txt, key)
print(f"Decrypted text: {decrypted_txt}")
