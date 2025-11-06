def vernam_encrypt(plain_text, key):
    plain_text = plain_text.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    
    if len(key) < len(plain_text):
        raise ValueError("Key must be at least as long as the plaintext")
    
    cipher_text = ""
    for p, k in zip(plain_text, key):
        if p.isalpha():
            encrypted_char = chr(((ord(p) - 65) ^ (ord(k) - 65)) + 65)
            cipher_text += encrypted_char
        else:
            cipher_text += p
    return cipher_text


def vernam_decrypt(cipher_text, key):
    key = key.upper().replace(" ", "")
    plain_text = ""
    for c, k in zip(cipher_text, key):
        if c.isalpha():
            decrypted_char = chr(((ord(c) - 65) ^ (ord(k) - 65)) + 65)
            plain_text += decrypted_char
        else:
            plain_text += c
    return plain_text


# Example
plain_text = "HELLO"
key = "XMCKL"

encrypted = vernam_encrypt(plain_text, key)
decrypted = vernam_decrypt(encrypted, key)

print("Plain Text:", plain_text)
print("Key:", key)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
