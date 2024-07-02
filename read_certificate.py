# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:41:10 2024

@author: Subham Divakar
"""

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import getpass

def read_and_display_certificate(cert_filename):
    try:
        with open(cert_filename, "rb") as cert_file:
            cert_data = cert_file.read()

            password = getpass.getpass(prompt="Enter password for the certificate (leave blank if not encrypted): ")
            password = password.encode('utf-8') if password else None

            certificate = None

            # Attempt to load as PEM certificate
            try:
                certificate = x509.load_pem_x509_certificate(cert_data, default_backend())
            except ValueError as e:
                if "Bad decrypt." in str(e):
                    print("PEM Load Error: Incorrect password or encrypted with a different algorithm.")
                else:
                    print(f"PEM Load Error: {e}")

            # If certificate loaded successfully as PEM
            if certificate is not None:
                print("Certificate Information:")
                print(f"  Subject: {certificate.subject}")
                print(f"  Issuer: {certificate.issuer}")
                print(f"  Validity:")
                print(f"    Not Before: {certificate.not_valid_before}")
                print(f"    Not After : {certificate.not_valid_after}")
                # Add more details as needed
                return

            # If not loaded as PEM, attempt to load as DER certificate (only if PEM decryption error did not occur)
            if certificate is None:
                try:
                    certificate = x509.load_der_x509_certificate(cert_data, default_backend())
                except ValueError as e:
                    print(f"DER Load Error: {e}")

                # If certificate loaded successfully as DER
                if certificate is not None:
                    print("Certificate Information (DER Format):")
                    print(f"  Subject: {certificate.subject}")
                    print(f"  Issuer: {certificate.issuer}")
                    print(f"  Validity:")
                    print(f"    Not Before: {certificate.not_valid_before}")
                    print(f"    Not After : {certificate.not_valid_after}")
                    # Add more details as needed
                    return

            # If neither PEM nor DER format was recognized
            if certificate is None:
                print(f"Error: '{cert_filename}' is not a valid PEM or DER certificate.")

    except FileNotFoundError:
        print(f"Error: File '{cert_filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("=== Certificate Details Viewer ===")
    cert_filename = input("Enter the path to the certificate file (.crt): ").strip()
    read_and_display_certificate(cert_filename)

if __name__ == "__main__":
    main()
