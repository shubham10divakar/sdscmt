# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 12:02:26 2024

@author: Subham Divakar
"""

from cryptography.hazmat.primitives.serialization import load_der_private_key, Encoding, PrivateFormat
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class DERtoPKCS12Converter:
    def __init__(self):
        pass

    def convert(self, der_file, pkcs12_file, password=None):
        try:
            with open(der_file, "rb") as f:
                der_data = f.read()
                private_key = load_der_private_key(der_data, password=password, backend=default_backend())

                pkcs12_data = private_key.private_bytes(
                    encoding=Encoding.PKCS12,
                    format=PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.BestAvailableEncryption(password)
                )

                with open(pkcs12_file, "wb") as pf:
                    pf.write(pkcs12_data)

        except FileNotFoundError:
            print(f"Error: File '{der_file}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    converter = DERtoPKCS12Converter()
    der_filename = input("Enter the DER filename (without extension): ").strip() + ".der"
    pkcs12_filename = input("Enter the PKCS#12 filename to save (without extension): ").strip() + ".pfx"
    password = input("Enter password for PKCS#12 (leave blank for no encryption): ").strip()
    converter.convert(der_filename, pkcs12_filename, password)
    print(f"Conversion from DER to PKCS#12 complete. Output saved to {pkcs12_filename}.")
