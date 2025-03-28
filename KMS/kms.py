from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os, base64, json

class SecureKeyManagement:
    def _init_(self):
        self.symmetric_keys = {}
        self.asymmetric_keys = {}

    def generate_symmetric_key(self, user_id):
        key = os.urandom(32)  # AES-256 key
        self.symmetric_keys[user_id] = key
        return base64.b64encode(key).decode()

    def generate_asymmetric_key_pair(self, user_id):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        
        self.asymmetric_keys[user_id] = {
            "private": private_key,
            "public": public_key
        }
        return {
            "private_key": private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ).decode(),
            "public_key": public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode()
        }
    
    def encrypt_with_symmetric_key(self, user_id, plaintext):
        key = self.symmetric_keys.get(user_id)
        if not key:
            return None
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        plaintext_padded = plaintext.ljust(16 * ((len(plaintext) // 16) + 1))
        ciphertext = encryptor.update(plaintext_padded.encode()) + encryptor.finalize()
        return base64.b64encode(iv + ciphertext).decode()
    
    def decrypt_with_symmetric_key(self, user_id, ciphertext):
        key = self.symmetric_keys.get(user_id)
        if not key:
            return None
        data = base64.b64decode(ciphertext)
        iv, encrypted_text = data[:16], data[16:]
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(encrypted_text) + decryptor.finalize()
        return plaintext.strip().decode()
    
    def encrypt_with_public_key(self, user_id, plaintext):
        public_key = self.asymmetric_keys.get(user_id, {}).get("public")
        if not public_key:
            return None
        ciphertext = public_key.encrypt(
            plaintext.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return base64.b64encode(ciphertext).decode()
    
    def decrypt_with_private_key(self, user_id, ciphertext):
        private_key = self.asymmetric_keys.get(user_id, {}).get("private")
        if not private_key:
            return None
        ciphertext = base64.b64decode(ciphertext)
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext.decode()
    
    def revoke_key(self, user_id):
        if user_id in self.symmetric_keys:
            del self.symmetric_keys[user_id]
        if user_id in self.asymmetric_keys:
            del self.asymmetric_keys[user_id]
        return f"Keys for user {user_id} revoked."

# Example Usage
skm = SecureKeyManagement()
user_id = "user123"

# Generate keys
sym_key = skm.generate_symmetric_key(user_id)
asym_keys = skm.generate_asymmetric_key_pair(user_id)

# Encryption & Decryption (Symmetric)
cipher_text = skm.encrypt_with_symmetric_key(user_id, "Hello, Secure World!")
plain_text = skm.decrypt_with_symmetric_key(user_id, cipher_text)

# Encryption & Decryption (Asymmetric)
cipher_text_asym = skm.encrypt_with_public_key(user_id, "Hello, Public Key!")
plain_text_asym = skm.decrypt_with_private_key(user_id, cipher_text_asym)

# Revoke keys
skm.revoke_key(user_id)

print("Symmetric Encryption:", cipher_text)
print("Decrypted Symmetric:", plain_text)
print("Asymmetric Encryption:", cipher_text_asym)
print("Decrypted Asymmetric:", plain_text_asym)
