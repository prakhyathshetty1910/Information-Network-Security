# Vigenère Cipher in Python

## Overview
The Vigenère Cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. It uses a keyword to shift each letter of the plaintext, making it harder to decipher without knowing the keyword.

This Python script implements the Vigenère Cipher, which can both encrypt and decrypt messages based on a user-provided key.

## Features
- **Encryption**: Encrypt a plaintext message using a provided keyword.
- **Decryption**: Decrypt a previously encrypted message using the same keyword.
- **Customizable Key**: Choose any key (string) for encryption and decryption.

## Requirements
- Python 3.x

## Installation
1. Clone this repository or download the script.
2. Ensure that Python 3.x is installed on your machine.
3. No additional libraries are needed. The script uses only built-in Python features.

## Usage

### Encryption
```python
from vigenere_cipher import encrypt

# Example usage
plaintext = "HELLO WORLD"
key = "KEY"
ciphertext = encrypt(plaintext, key)
print(f"Encrypted Text: {ciphertext}")
