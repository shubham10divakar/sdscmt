from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from cryptography import x509
from datetime import datetime, timedelta
import getpass

def generate_self_signed_cert(hostname, organization=None, country=None, valid_days=365):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    subject_attributes = [
        x509.NameAttribute(NameOID.COMMON_NAME, hostname),
    ]

    if organization:
        subject_attributes.append(x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization))
    if country:
        subject_attributes.append(x509.NameAttribute(NameOID.COUNTRY_NAME, country))

    subject = x509.Name(subject_attributes)

    valid_from = datetime.utcnow()
    valid_to = valid_from + timedelta(days=valid_days)

    builder = x509.CertificateBuilder()
    builder = builder.subject_name(subject)
    builder = builder.issuer_name(subject)
    builder = builder.not_valid_before(valid_from)
    builder = builder.not_valid_after(valid_to)
    builder = builder.serial_number(x509.random_serial_number())
    builder = builder.public_key(private_key.public_key())
    builder = builder.add_extension(
        x509.SubjectAlternativeName([
            x509.DNSName(hostname),
        ]),
        critical=False,
    )

    certificate = builder.sign(
        private_key=private_key,
        algorithm=hashes.SHA256(),
        backend=default_backend()
    )

    return private_key, certificate

def save_private_key(private_key, filename, password=None):
    encryption_algorithm = serialization.BestAvailableEncryption(password) if password else serialization.NoEncryption()
    with open(filename, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=encryption_algorithm
        ))

def save_certificate(certificate, filename):
    with open(filename, "wb") as f:
        f.write(certificate.public_bytes(encoding=serialization.Encoding.PEM))

def main():
    print("=== Self-Signed Certificate Generator ===")
    hostname = input("Enter the hostname: ").strip()
    organization = input("Enter the organization (optional): ").strip() or None
    country = input("Enter the country (optional): ").strip() or None
    valid_days = int(input("Enter the number of days the certificate is valid for: ").strip())

    private_key, certificate = generate_self_signed_cert(hostname, organization, country, valid_days)

    key_filename = input("Enter the filename to save the private key(ending with .key): ").strip()
    cert_filename = input("Enter the filename to save the certificate(endind with .crt): ").strip()
    password = getpass.getpass(prompt="Enter password to encrypt the private key (leave blank for no encryption): ")
    password = password.encode('utf-8') if password else None

    save_private_key(private_key, key_filename, password)
    save_certificate(certificate, cert_filename)

    print(f"Private key saved to {key_filename}")
    print(f"Certificate saved to {cert_filename}")

if __name__ == "__main__":
    main()
