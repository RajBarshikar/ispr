from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


key = b'Sixteen byte key'
iv = b'Sixteen byte iv.'   

cipher = AES.new(key, AES.MODE_CBC, iv)


plain_text = b"HELLO THIS IS AES ENCRYPTION"


cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
print("Encrypted:", cipher_text.hex())


decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_text = unpad(decipher.decrypt(cipher_text), AES.block_size)
print("Decrypted:", decrypted_text.decode())
