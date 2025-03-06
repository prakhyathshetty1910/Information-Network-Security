# Hill Cipher - Python Implementation

## Overview

This is a Python implementation of the **Hill Cipher**, a classical encryption algorithm that uses matrix operations to encrypt and decrypt messages. The Hill Cipher encrypts and decrypts text using a square key matrix, and it works with blocks of text of the size corresponding to the matrix dimension.

## Features

- Encrypt and decrypt messages using a square key matrix.
- Handles both uppercase and lowercase English alphabetic characters.
- Uses modular arithmetic to wrap text within the 26-letter alphabet.

## Prerequisites

- Python 3.x
- Required libraries:
  - `numpy`: For matrix operations and handling key matrices.

To install the required dependencies, use the following command:

```bash
pip install numpy
```

## Encryption
The plaintext is broken into blocks of letters, with each block's size corresponding to the dimensions of the key matrix.
Each letter is converted to a number (A = 0, B = 1, ..., Z = 25).
The key matrix is multiplied by the plaintext matrix, and the resulting values are taken modulo 26 to get the ciphertext.
The resulting numbers are converted back into letters to form the encrypted message.
## Decryption
The inverse of the key matrix (mod 26) is calculated.
The ciphertext is multiplied by the inverse key matrix.
The result is taken modulo 26 to recover the original plaintext.
