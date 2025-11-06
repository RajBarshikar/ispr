import random
import string

def generate_random_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def one_time_pad_encrypt(plain_text, key):
    plain_text = plain_text.upper().replace(" ", "")
    key = key.upper().replace(" ", "")

    if len(key) < len(plain_text):
        raise ValueError("Key must be at least as long as the plaintext")

    cipher_text = ""
    for p, k in zip(plain_text, key):
        encrypted_char = chr(((ord(p) - 65) ^ (ord(k) - 65)) + 65)
        cipher_text += encrypted_char

    return cipher_text


def one_time_pad_decrypt(cipher_text, key):
    key = key.upper().replace(" ", "")
    plain_text = ""

    for c, k in zip(cipher_text, key):
        decrypted_char = chr(((ord(c) - 65) ^ (ord(k) - 65)) + 65)
        plain_text += decrypted_char

    return plain_text


# Example
plain_text = "HELLOWORLD"
key = generate_random_key(len(plain_text))

encrypted = one_time_pad_encrypt(plain_text, key)
decrypted = one_time_pad_decrypt(encrypted, key)

print("Plain Text :", plain_text)
print("Key        :", key)
print("Encrypted  :", encrypted)
print("Decrypted  :", decrypted)
