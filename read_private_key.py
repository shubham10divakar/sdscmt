from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_der_private_key
import getpass

def read_and_display_private_key(key_filename):
    try:
        with open(key_filename, "rb") as key_file:
            key_data = key_file.read()
            
            password = getpass.getpass(prompt="Enter password for the private key (leave blank if not encrypted): ")
            password = password.encode('utf-8') if password else None

            private_key = None
            password_error = False

            # Attempt to load as PEM private key
            try:
                private_key = serialization.load_pem_private_key(
                    key_data,
                    password=password,
                    backend=default_backend()
                )
            except ValueError as e:
                if "Bad decrypt." in str(e):
                    password_error = True
                    print("PEM Load Error: Incorrect password or encrypted with a different algorithm.")
                else:
                    print(f"PEM Load Error: {e}")

            # If private_key is loaded successfully as PEM
            if private_key is not None:
                print("Private Key Information:")
                print(f"  Type: {type(private_key)}")
                print(f"  Size: {private_key.key_size} bits")
                print("  Key Data:")
                print(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                ).decode('utf-8'))
                print("  Details:")
                print(f"    Modulus: {private_key.private_numbers().public_numbers.n}")
                print(f"    Public Exponent: {private_key.private_numbers().public_numbers.e}")
                return

            # Attempt to load as DER private key (only if PEM decryption error did not occur)
            if private_key is None and not password_error:
                try:
                    private_key = serialization.load_der_private_key(
                        key_data,
                        password=password,
                        backend=default_backend()
                    )
                except ValueError as e:
                    print(f"DER Load Error: {e}")

                # If private_key is loaded successfully as DER
                if private_key is not None:
                    print("Private Key Information (DER Format):")
                    print(f"  Type: {type(private_key)}")
                    print(f"  Size: {private_key.key_size} bits")
                    print("  Key Data:")
                    print(private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.PKCS8,
                        encryption_algorithm=serialization.NoEncryption()
                    ).decode('utf-8'))
                    print("  Details:")
                    print(f"    Modulus: {private_key.private_numbers().public_numbers.n}")
                    print(f"    Public Exponent: {private_key.private_numbers().public_numbers.e}")
                    return

            # If neither PEM nor DER format was recognized
            if private_key is None and not password_error:
                print(f"Error: '{key_filename}' is not a valid PEM or DER private key.")

    except FileNotFoundError:
        print(f"Error: File '{key_filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("=== Private Key Details Viewer ===")
    key_filename = input("Enter the path to the private key file: ").strip()
    read_and_display_private_key(key_filename)

if __name__ == "__main__":
    main()
