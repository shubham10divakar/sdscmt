# Secure Data SSL Certificate Management Tool (SDSCMT)

Secure Data Certificate Format Converter (SDCFC) is a powerful tool for generating and managing self signed ssl certificates and private key files, offering seamless conversion between PEM, DER, and PKCS12 formats as well. Whether you need to generate, convert, or manage self signed ssl certificates, SDSCMT provides a user-friendly interface to get the job done.

## Other Tools From SD(Secure Data) series
1. SDCFC(Tool for key conversion from one format to another) - https://pypi.org/project/sdcfc/ 
2. SDSCMT - https://pypi.org/project/sdscmt/

## Features
- Generate Self Signed Certificates
- Validate existing self signed ssl certs
- Convert PEM to DER
- Convert DER to PEM
- Convert PEM to PKCS#12
- Convert PKCS#12 to PEM
- Convert DER to PKCS#12

## Installation
To install SDSCMT, use pip:
```sh
pip install sdscmt

Usage
Command Line Interface

After installing, you can use the tool via command line:

sh

sdscmt

Example Usage

python

to invoke the mainmenu...
import sdscmt
# Now you can use functions or classes defined in sdscmt module
sdscmt.main()
Note:- when you are using path(absolute or relative paths) to files donot enclose them in either '' or "" quotes in any environment.
ex- usaage

=== SDSCMT(Secure Data Self Signed SSL Cert Management Tool) ===
One stop cert generation and management tool.
self signed cert generation and cert management at ease......

Created by Subham Divakar

Connect with me:
- LinkedIn: https://www.linkedin.com/in/subham-divakar-a7420a12a/
- GitHub: https://github.com/shubham10divakar
- Portfolio: https://shubham10divakar.github.io/showcasehub/


>>> import sdscmt
>>> sdscmt.main();
=== SDSCMT(Secure Data Self Signed SSL Cert Management Tool) ===
One stop cert generation and management tool.
self signed cert generation and cert management at ease......

Created by Subham Divakar

Connect with me:
- LinkedIn: https://www.linkedin.com/in/subham-divakar-a7420a12a/
- GitHub: https://github.com/shubham10divakar
- Portfolio: https://shubham10divakar.github.io/showcasehub/


1. Generate self-signed certificate
2. Validate and display existing private key
3. Validate and display existing cert(crt) file
3. Encrypt private key (recommended)
4. Cert Conversion Tool to convert cert from one type(DER, PKCS12, PEM) to another ones(DER, PKCS12, PEM)
Enter your choice (1/2/3/4): 1
=== Self-Signed Certificate Generator ===
Enter the hostname: demo
Enter the organization (optional): gbu
Enter the country (optional): IN
Enter the number of days the certificate is valid for: 365
Enter the filename to save the private key(ending with .key): gbu_private_key.key
Enter the filename to save the certificate(endind with .crt): gbu_cert.crt
Enter password to encrypt the private key (leave blank for no encryption):
Private key saved to gbu_private_key.key
Certificate saved to gbu_cert.crt
```sh

##Connect with Me

    LinkedIn: https://www.linkedin.com/in/subham-divakar-a7420a12a/
    GitHub: https://github.com/shubham10divakar
    Portfolio: https://shubham10divakar.github.io/showcasehub/

##Feedback

Your feedback is important! Please share your thoughts and suggestions.
License

This project is licensed under the MIT License.