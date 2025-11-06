def caesar_encrypt(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            cipher_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            cipher_text += char
    return cipher_text

def caesar_decrypt(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            plain_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            plain_text += char
    return plain_text

text = "ATTACKATDAWN"
shift = 3

encrypted = caesar_encrypt(text, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Plaintext:", text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
