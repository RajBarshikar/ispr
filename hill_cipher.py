import numpy as np
from math import gcd

def letter_to_number(char):
    return ord(char.upper()) - ord('A')

def number_to_letter(num):
    return chr((num % 26) + ord('A'))

def modular_inverse(number, mod=26):
    for x in range(1, mod):
        if (number * x) % mod == 1:
            return x
    return None

def hill_encrypt(plain_text, key_matrix):
    plain_text = plain_text.replace(" ", "").upper()
    while len(plain_text) % 3 != 0:
        plain_text += 'X'
    cipher_text = ""
    for i in range(0, len(plain_text), 3):
        block = plain_text[i:i+3]
        vector = np.array([[letter_to_number(block[0])],
                           [letter_to_number(block[1])],
                           [letter_to_number(block[2])]])
        encrypted_vector = np.dot(key_matrix, vector) % 26
        for j in range(3):
            cipher_text += number_to_letter(encrypted_vector[j][0])
    return cipher_text

def hill_decrypt(cipher_text, key_matrix):
    cipher_text = cipher_text.replace(" ", "").upper()
    determinant = int(round(np.linalg.det(key_matrix))) % 26
    if gcd(determinant, 26) != 1:
        raise ValueError("Key matrix is not invertible modulo 26")
    determinant_inverse = modular_inverse(determinant, 26)
    adjugate_matrix = np.round(np.linalg.inv(key_matrix) * np.linalg.det(key_matrix)).astype(int)
    inverse_key_matrix = (determinant_inverse * adjugate_matrix) % 26
    inverse_key_matrix = inverse_key_matrix.astype(int)
    decrypted_text = ""
    for i in range(0, len(cipher_text), 3):
        block = cipher_text[i:i+3]
        vector = np.array([[letter_to_number(block[0])],
                           [letter_to_number(block[1])],
                           [letter_to_number(block[2])]])
        decrypted_vector = np.dot(inverse_key_matrix, vector) % 26
        for j in range(3):
            decrypted_text += number_to_letter(decrypted_vector[j][0])
    return decrypted_text

if __name__ == "__main__":
    key_matrix = np.array([[6, 24, 1],
                           [13, 16, 10],
                           [20, 17, 15]])
    plain_text = "ACT"
    cipher_text = hill_encrypt(plain_text, key_matrix)
    print("Encrypted:", cipher_text)
    decrypted_text = hill_decrypt(cipher_text, key_matrix)
    print("Decrypted:", decrypted_text)
