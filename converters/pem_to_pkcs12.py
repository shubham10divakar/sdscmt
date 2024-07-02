# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 12:01:25 2024

@author: Subham Divakar
"""

from cryptography.hazmat.primitives.serialization import load_pem_private_key, Encoding, PrivateFormat
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class PEMtoPKCS12Converter:
    def __init__(self):
        pass

    def convert(self, pem_file, pkcs12_file, password=None):
        try:
            with open(pem_file, "rb") as f:
                pem_data = f.read()
                private_key = load_pem_private_key(pem_data, password=password, backend=default_backend())

                pkcs12_data = private_key.private_bytes(
                    encoding=Encoding.PKCS12,
                    format=PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.BestAvailableEncryption(password)
                )

                with open(pkcs12_file, "wb") as pf:
                    pf.write(pkcs12_data)

        except FileNotFoundError:
            print(f"Error: File '{pem_file}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    converter = PEMtoPKCS12Converter()
    pem_filename = input("Enter the PEM filename (without extension): ").strip() + ".pem"
    pkcs12_filename = input("Enter the PKCS#12 filename to save (without extension): ").strip() + ".pfx"
    password = input("Enter password for PKCS#12 (leave blank for no encryption): ").strip()
    converter.convert(pem_filename, pkcs12_filename, password)
    print(f"Conversion from PEM to PKCS#12 complete. Output saved to {pkcs12_filename}.")
