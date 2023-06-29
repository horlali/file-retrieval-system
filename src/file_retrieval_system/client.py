import os
from base64 import b64decode

import Pyro4
import streamlit as st
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

from utils.constants import CLIENT_FILE_DIR, HOST, OBJECT_ID, PORT

# Connect to the server
URI = f"PYRO:{OBJECT_ID}@{HOST}:{PORT}"
server = Pyro4.Proxy(URI)

# Generate a random session key
session_key = get_random_bytes(16)

# Encrypt the session key using the server's public key
server_public_key_data = server.get_public_key()["data"]
decoded_server_public_key = b64decode(server_public_key_data)

server_public_key = RSA.import_key(decoded_server_public_key)
cipher_rsa = PKCS1_OAEP.new(server_public_key)
encrypted_session_key = cipher_rsa.encrypt(session_key)


def list_files():
    st.header("Files on server")
    st.write("The following files are available on the server:")
    files = server.list_files()

    if not files:
        st.write("No files found.")
    else:
        for filename in files:
            st.markdown(f"-     {filename}")


def download_file_unsecurely():
    st.header("Unencrypted file exchange")
    st.write("Downloading files from this way does not require and key exchange.")
    st.header("Retrieve files")
    filename = st.text_input("Enter filename to download")

    if st.button("Download"):
        try:
            file_contents = server.get_file(filename)

            if file_contents:
                data_bytes = b64decode(file_contents["data"])
                data_str = data_bytes.decode()

            with open(os.path.join(CLIENT_FILE_DIR, filename), "wb") as f:
                f.write(data_str.encode())

            st.success(f"File {filename} downloaded successfully!")
            st.write("The contents of the file are:")
            st.text(data_str)

        except FileNotFoundError:
            st.error(f"The file {filename} does not exist on the server.")

        except IsADirectoryError:
            st.error("Please enter a filename on the server directory to download.")


def download_file_securely():
    st.header("Encrypted file exchange")
    st.write("Downloading files this way requires key exchange.")
    st.header("Retrieve files")
    filename = st.text_input("Enter secure filename to download")

    if st.button("Download files securely"):
        try:
            nonce, tag, ciphertext = server.get_secure_file(
                filename,
                encrypted_session_key,
            )

            nonce = b64decode(nonce["data"])
            tag = b64decode(tag["data"])
            ciphertext = b64decode(ciphertext["data"])

            # Decrypt the file content using the session key
            cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
            file_content = cipher_aes.decrypt_and_verify(ciphertext, tag)

            with open(os.path.join(CLIENT_FILE_DIR, filename), "wb") as f:
                f.write(file_content)

            st.success(f"File {filename} downloaded successfully!")
            st.write("The contents of the file is:")
            st.text(file_content.decode("utf-8"))

        except FileNotFoundError:
            st.error(f"The file {filename} does not exist on the server.")

        except IsADirectoryError:
            st.error("Please enter a filename on the server directory to download.")


def app():
    st.title("File Retrieval System")

    # Files on server
    list_files()

    # Download files without encryption
    download_file_unsecurely()

    # Download files with encryption
    download_file_securely()


if __name__ == "__main__":
    app()
