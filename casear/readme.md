# Caesar Cipher in Python

This is a Python implementation of the Caesar Cipher, a classic encryption technique. The Caesar Cipher shifts each letter in the plaintext by a fixed number of positions down the alphabet.

## How It Works

The Caesar Cipher works by shifting the letters of the alphabet by a certain number (key). For example, if the key is 3, then:
- 'A' becomes 'D'
- 'B' becomes 'E'
- 'C' becomes 'F'
- And so on.

The shift is applied to both lowercase and uppercase letters, while non-alphabetic characters (like numbers and punctuation) remain unchanged.

## Features

- Encrypt a message using the Caesar Cipher.
- Decrypt a message using the Caesar Cipher.
- Support for both lowercase and uppercase letters.
- Handles non-alphabetic characters without modification.

## Installation

1. Clone the repository or download the script:

    ```bash
    git clone https://github.com/yourusername/caesar-cipher-python.git
    ```

2. Navigate to the project directory:

    ```bash
    cd caesar-cipher-python
    ```

3. (Optional) Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

## Usage

### Encrypt a message

To encrypt a message, use the `encrypt()` function, passing the plaintext and the key (shift value):

```python
from caesar_cipher import CaesarCipher

cipher = CaesarCipher(key=3)
encrypted_message = cipher.encrypt("Hello World!")
print(f"Encrypted Message: {encrypted_message}")
