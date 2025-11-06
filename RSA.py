# RSA Algorithm Implementation

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

def rsa_key_generation(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = mod_inverse(e, phi)

    return (e, n), (d, n)

def encrypt(plain_text, public_key):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in plain_text]
    return cipher

def decrypt(cipher_text, private_key):
    d, n = private_key
    plain = [chr((char ** d) % n) for char in cipher_text]
    return ''.join(plain)

# Example
p = 11
q = 13
public_key, private_key = rsa_key_generation(p, q)

print("Public Key:", public_key)
print("Private Key:", private_key)

plain_text = "HELLO"
print("\nOriginal Text:", plain_text)

cipher_text = encrypt(plain_text, public_key)
print("Encrypted Text:", cipher_text)

decrypted_text = decrypt(cipher_text, private_key)
print("Decrypted Text:", decrypted_text)
