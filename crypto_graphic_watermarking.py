import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature


PRIVATE_KEY_FILE = 'private_key.pem'
PUBLIC_KEY_FILE = 'public_key.pem'

def generate_keys():
    """
    Generates and saves a new RSA private and public key pair.
    """
    print(f"Generating new key pair...")
    try:
        
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )


        pem_private = private_key.private_bytes(
           encoding=serialization.Encoding.PEM,
           format=serialization.PrivateFormat.TraditionalOpenSSL,
           encryption_algorithm=serialization.NoEncryption()
        )
        with open(PRIVATE_KEY_FILE, 'wb') as f:
            f.write(pem_private)

       
        public_key = private_key.public_key()
        pem_public = public_key.public_bytes(
           encoding=serialization.Encoding.PEM,
           format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(PUBLIC_KEY_FILE, 'wb') as f:
            f.write(pem_public)

        print(f"Success: Keys generated and saved as:")
        print(f"  Private Key: {PRIVATE_KEY_FILE}")
        print(f"  Public Key: {PUBLIC_KEY_FILE}")
        print("-" * 30)

    except Exception as e:
        print(f"Error generating keys: {e}")

def sign_file(image_path):
    """
    Generates a digital signature for a given file using the private key.
    """
    if not os.path.exists(PRIVATE_KEY_FILE):
        print(f"Error: Private key '{PRIVATE_KEY_FILE}' not found.")
        print("Please generate keys first (Option 1).")
        return

    if not os.path.exists(image_path):
        print(f"Error: Image file not found at '{image_path}'")
        return

    signature_file = image_path + ".sig"
    print(f"Signing '{image_path}'...")

    try:
        
        with open(PRIVATE_KEY_FILE, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
            )

        
        with open(image_path, "rb") as f:
            image_data = f.read()

       
        signature = private_key.sign(
            image_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        # --- Save the Signature ---
        with open(signature_file, "wb") as f:
            f.write(signature)

        print(f"Success: Image signed.")
        print(f"Signature saved to: {signature_file}")
        print("-" * 30)

    except Exception as e:
        print(f"Error during signing: {e}")

def verify_file(image_path):
    """
    Verifies the digital signature of a file using the public key.
    """
    if not os.path.exists(PUBLIC_KEY_FILE):
        print(f"Error: Public key '{PUBLIC_KEY_FILE}' not found.")
        print("Please generate keys first (Option 1).")
        return

    if not os.path.exists(image_path):
        print(f"Error: Image file not found at '{image_path}'")
        return

    signature_file = image_path + ".sig"
    if not os.path.exists(signature_file):
        print(f"Error: Signature file not found at '{signature_file}'")
        return
        
    print(f"Verifying '{image_path}'...")

    try:
        
        with open(PUBLIC_KEY_FILE, "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read()
            )

        
        with open(image_path, "rb") as f:
            image_data = f.read()

       
        with open(signature_file, "rb") as f:
            signature = f.read()

        
        public_key.verify(
            signature,
            image_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        print("\n" + "=" * 30)
        print("VERIFICATION SUCCESS")
        print("   The signature is valid.")
        print("   This proves the image is authentic and has not been tampered with.")
        print("=" * 30 + "\n")

    except InvalidSignature:
        print("\n" + "!" * 30)
        print("VERIFICATION FAILED")
        print("   The signature is INVALID!")
        print("   The image may be a fake or has been modified.")
        print("!" * 30 + "\n")
    except Exception as e:
        print(f"An error occurred during verification: {e}")

def main():
    """
    Main interactive loop for the tool.
    """
    print("--- Image Digital Signature Tool ---")
    while True:
        print("\nWhat would you like to do?")
        print("  [1] Generate a new key pair")
        print("  [2] Sign an image")
        print("  [3] Verify an image")
        print("  [4] Quit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            generate_keys()

        elif choice == '2':
            image_path = input("Enter the path to the image you want to sign: ")
            sign_file(image_path)

        elif choice == '3':
            image_path = input("Enter the path to the image you want to verify: ")
            verify_file(image_path)

        elif choice == '4':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()