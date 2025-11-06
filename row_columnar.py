import math

def row_columnar_encrypt(plain_text, key):
    plain_text = plain_text.replace(" ", "").upper()
    key_order = sorted(list(key))
    num_cols = len(key)
    num_rows = math.ceil(len(plain_text) / num_cols)

    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    index = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if index < len(plain_text):
                matrix[i][j] = plain_text[index]
                index += 1

    cipher_text = ""
    for char in key_order:
        col = key.index(char)
        for row in range(num_rows):
            if matrix[row][col] != '':
                cipher_text += matrix[row][col]

    return cipher_text


def row_columnar_decrypt(cipher_text, key):
    key_order = sorted(list(key))
    num_cols = len(key)
    num_rows = math.ceil(len(cipher_text) / num_cols)

    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    col_lengths = [num_rows] * num_cols
    total_cells = num_rows * num_cols
    extra = total_cells - len(cipher_text)
    if extra > 0:
        for i in range(extra):
            col_lengths[-(i+1)] -= 1

    index = 0
    for char in key_order:
        col = key.index(char)
        for row in range(col_lengths[col]):
            matrix[row][col] = cipher_text[index]
            index += 1

    plain_text = ""
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] != '':
                plain_text += matrix[i][j]

    return plain_text


# Example
plain_text = "INFORMATIONSECURITY"
key = "CIPHER"

encrypted = row_columnar_encrypt(plain_text, key)
decrypted = row_columnar_decrypt(encrypted, key)

print("Plain Text :", plain_text)
print("Key        :", key)
print("Encrypted  :", encrypted)
print("Decrypted  :", decrypted)
