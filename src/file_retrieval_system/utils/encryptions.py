import os

import rsa

from file_retrieval_system.utils.constants import KEY_FILE_DIR


def create_keys():
    """
    generating public and private keys using the rsa library
    """
    publicKey, privateKey = rsa.newkeys(1024)

    with open(os.path.join(KEY_FILE_DIR, "publicKey.pem"), "wb") as p:
        p.write(publicKey.save_pkcs1("PEM"))

    with open(os.path.join(KEY_FILE_DIR, "privateKey.pem"), "wb") as p:
        p.write(privateKey.save_pkcs1("PEM"))


def encrypt(message, key):
    """
    Encrypts a message using the given key
    """
    return rsa.encrypt(message.encode("ascii"), key)


def decrypt(ciphertext, key):
    """
    Decrypts a ciphertext using the given key
    """
    try:
        return rsa.decrypt(ciphertext, key).decode("ascii")
    except Exception:
        return False


def sign(message, key):
    """
    Signs a message using the given key
    """
    return rsa.sign(message.encode("ascii"), key, "SHA-1")


def verify(message, signature, key):
    """
    Verifies a message using the given key
    """
    try:
        return rsa.verify(message.encode("ascii"), signature, key) == "SHA-1"
    except Exception:
        return False


def load_keys():
    """
    load the encryption key
    """
    with open(os.path.join(KEY_FILE_DIR, "publicKey.pem"), "rb") as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())

    with open(os.path.join(KEY_FILE_DIR, "privateKey.pem"), "rb") as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())

    return privateKey, publicKey
