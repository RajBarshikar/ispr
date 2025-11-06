def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    key_matrix = []
    used = set()

    for char in key:
        if char.isalpha() and char not in used:
            used.add(char)
            key_matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            used.add(char)
            key_matrix.append(char)

    matrix = [key_matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix


def prepare_text(text, for_encryption=True):
    text = text.upper().replace("J", "I")
    prepared = ""
    i = 0
    while i < len(text):
        if not text[i].isalpha():
            i += 1
            continue
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) and text[i + 1].isalpha() else 'X'

        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2

    if len(prepared) % 2 != 0:
        prepared += 'X'
    return prepared


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None


def playfair_encrypt(plain_text, matrix):
    text = prepare_text(plain_text)
    cipher_text = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:
            cipher_text += matrix[row_a][(col_a + 1) % 5]
            cipher_text += matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            cipher_text += matrix[(row_a + 1) % 5][col_a]
            cipher_text += matrix[(row_b + 1) % 5][col_b]
        else:
            cipher_text += matrix[row_a][col_b]
            cipher_text += matrix[row_b][col_a]

    return cipher_text


def playfair_decrypt(cipher_text, matrix):
    plain_text = ""

    for i in range(0, len(cipher_text), 2):
        a, b = cipher_text[i], cipher_text[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:
            plain_text += matrix[row_a][(col_a - 1) % 5]
            plain_text += matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            plain_text += matrix[(row_a - 1) % 5][col_a]
            plain_text += matrix[(row_b - 1) % 5][col_b]
        else:
            plain_text += matrix[row_a][col_b]
            plain_text += matrix[row_b][col_a]

    return plain_text


# Example
key = "MONARCHY"
plain_text = "INSTRUMENTS"

matrix = generate_key_matrix(key)
cipher_text = playfair_encrypt(plain_text, matrix)
decrypted_text = playfair_decrypt(cipher_text, matrix)

print("Key Matrix:")
for row in matrix:
    print(row)

print("\nPlain Text:", plain_text)
print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypted_text)
