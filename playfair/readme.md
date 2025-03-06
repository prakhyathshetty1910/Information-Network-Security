# Playfair Cipher - Python Implementation

## Overview

This is a Python implementation of the **Playfair Cipher**, a digraph substitution cipher that encrypts pairs of letters. The cipher uses a 5x5 matrix of letters (usually the English alphabet) and applies a set of rules to encrypt or decrypt the plaintext message.

## Features

- Encrypts and decrypts messages using a 5x5 Playfair cipher matrix.
- Supports both uppercase and lowercase English alphabetic characters.
- Ignores non-alphabetical characters and treats 'J' and 'I' as the same letter (standard practice in Playfair Cipher).
- Can handle text of any length by adding filler letters (usually 'X') when needed.

## Prerequisites

- Python 3.x

## Installation

No external dependencies are required for this implementation. However, ensure you are using Python 3.x.

## How Playfair Cipher Works

1. **Key Matrix**: The key matrix is a 5x5 grid that contains a permutation of the letters of the alphabet. Typically, 'J' is excluded from the matrix and treated as 'I'.
2. **Digraphs**: The plaintext is split into digraphs (pairs of two letters). If there is an odd number of letters, a filler letter (commonly 'X') is added to the end of the message.
3. **Encryption Rules**:
    - If both letters in a digraph are the same (or only one letter remains), insert a filler letter (usually 'X') between them.
    - If the letters appear in the same row of the matrix, replace them with the letters immediately to their right (wrap around to the start of the row if necessary).
    - If the letters appear in the same column, replace them with the letters immediately below (wrap around to the top of the column if necessary).
    - If the letters form a rectangle, swap the letters with the ones in the same row but opposite corners of the rectangle.

4. **Decryption**: The decryption follows the reverse of the encryption rules.

## Usage

### Example

```python
from playfair import PlayfairCipher

# Create an instance of the Playfair cipher with a custom key
key = "MONARCHY"
cipher = PlayfairCipher(key)

# Encrypt a message
plaintext = "HELLO"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the message
decrypted_text = cipher.decrypt(ciphertext)
print("Decrypted Text:", decrypted_text)
