# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:44:56 2024

@author: Subham Divakar
"""

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import hmac, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_der_private_key
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_der_public_key
from cryptography.x509 import Name, NameAttribute
from cryptography.x509.oid import NameOID
from cryptography import x509
from datetime import datetime, timedelta
from .read_private_key import main as validate_key
from .generate_self_signed_cert import main as generate_self_signed_cert
from .read_certificate import main as read_cert
import os
from .cert_conversion_tool import main as cert_conversion_tool


def main():
    print("=== SDSCMT(Secure Data Self Signed SSL Cert Management Tool) ===")
    print("One stop cert generation and management tool.")
    print("self signed cert generation and cert management at ease......\n")
    
    print("Created by Subham Divakar\n")
    print("Connect with me:")
    print("- LinkedIn: https://www.linkedin.com/in/subham-divakar-a7420a12a/")
    print("- GitHub: https://github.com/shubham10divakar")
    print("- Portfolio: https://shubham10divakar.github.io/showcasehub/")
    print("\n")

    print("1. Generate self-signed certificate")
    print("2. Validate and display existing private key")
    print("3. Validate and display existing cert(crt) file")
    print("3. Encrypt private key (recommended)")
    print("4. Cert Conversion Tool to convert cert from one type(DER, PKCS12, PEM) to another ones(DER, PKCS12, PEM)")
    #print("5. Convert DER to PEM")
    #print("4. Encrypt certificate (optional)")
    

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '2':
        validate_key()
        #key_filename = input("Enter the path to the existing private key file: ").strip()
        #password = input("Enter password for decryption: ").strip()
        #validate_and_display_key(key_filename, password)
        return

    elif choice == '1':
        generate_self_signed_cert()
        #print('')
    
    elif choice == '3':
        read_cert()
        #print('')
    
    elif choice == '4':
        cert_conversion_tool()
        #print('')
        
    # elif choice == '5':
    #     print('')

        

if __name__ == "__main__":
    main()
