
# Monoalphabetic Cipher - Python Implementation

## Overview

This is a Python implementation of the **Monoalphabetic Cipher**, a substitution cipher where each letter of the plaintext is replaced by another letter from the alphabet. In this version, each letter of the alphabet maps to a unique letter of the alphabet in a fixed, one-to-one correspondence.

## Features

- Encrypts and decrypts messages using a simple monoalphabetic substitution cipher.
- Allows for custom substitution key where each letter maps to a different letter.
- Supports both uppercase and lowercase English alphabetic characters.
- Handles any length of plaintext and ciphertext, including spaces and punctuation.

## Prerequisites

- Python 3.x

## Installation

This implementation does not have any external dependencies and can be used directly with Python 3.x.

## How Monoalphabetic Cipher Works

1. **Key**: A key is a string of 26 letters of the alphabet, which determines the substitution. Each letter of the plaintext is replaced by the corresponding letter from the key. The key should contain every letter exactly once.
   
2. **Encryption**:
    - The plaintext is replaced letter by letter with the corresponding letter from the key.
    - Both uppercase and lowercase letters are substituted based on the key.

3. **Decryption**:
    - The ciphertext is substituted back using the reverse mapping of the key.

4. **Important**:
    - This cipher is vulnerable to frequency analysis, and using a random key improves security.
    - The key should not repeat or miss any letters of the alphabet.

## Usage

### Example

```python
from monoalphabetic import MonoalphabeticCipher

# Define the substitution key (must be a permutation of the alphabet)
key = "QAZWSXEDCRFVTGBYHNUJMIKOLP"
cipher = MonoalphabeticCipher(key)

# Encrypt a message
plaintext = "HELLO WORLD"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the message
decrypted_text = cipher.decrypt(ciphertext)
print("Decrypted Text:", decrypted_text)
