from base64 import b64decode

import Pyro4
import streamlit as st
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Pyro4.errors import CommunicationError

from file_retrieval_system.utils.constants import HOST, OBJECT_ID, PORT
from file_retrieval_system.utils.exceptions import CannotDownloadFile

# Connect to the server
URI = f"PYRO:{OBJECT_ID}@{HOST}:{PORT}"
server = Pyro4.Proxy(URI)

# Generate a random session key
session_key = get_random_bytes(16)


# Encrypt the session key using the server's public key
def encrypt_session_key():
    try:
        server_public_key_data = server.get_public_key()["data"]
        decoded_server_public_key = b64decode(server_public_key_data)

        server_public_key = RSA.import_key(decoded_server_public_key)
        cipher_rsa = PKCS1_OAEP.new(server_public_key)
        encrypted_session_key = cipher_rsa.encrypt(session_key)

        return encrypted_session_key

    except CommunicationError:
        st.error("The server is not running.")


def list_files():
    try:
        files = server.list_files()
        if not files:
            return []
        else:
            return [file for file in files]

    except CommunicationError:
        st.error("The server is not running.")


def list_files_on_server():
    try:
        st.header("Files on server")
        st.write("The following files are available on the server:")
        files = server.list_files()

        if not files:
            st.write("No files found.")
        else:
            for filename in files:
                st.markdown(f"-     {filename}")

    except CommunicationError:
        st.error("The server is not running.")


def download_file_unsecurely():
    st.header("Unencrypted file exchange")
    st.write("Downloading files from this way does not require and key exchange.")

    files = list_files() or []
    selected_file = st.selectbox("Please select a file to download", files)

    if selected_file:
        try:
            file_contents = server.get_file(selected_file)

            if file_contents:
                data_bytes = b64decode(file_contents["data"])
                data_str = data_bytes.decode()
            else:
                raise CannotDownloadFile("The selected file could not be downloaded.")

            if st.download_button(
                data=data_bytes, file_name=selected_file, label="Download file"
            ):
                st.success(f"File {selected_file} downloaded successfully!")
                st.write("The contents of the file are:")
                st.text(data_str)

        except FileNotFoundError:
            st.error(f"The file {selected_file} does not exist on the server.")

        except IsADirectoryError:
            st.error("Please enter a filename on the server directory to download.")

        except CommunicationError:
            st.error("The server is not running.")

        except CannotDownloadFile:
            st.error("The file could not be downloaded.")


def download_file_securely():
    st.header("Encrypted file exchange")
    st.write("Downloading files this way requires key exchange.")

    files = list_files() or []
    selected_file = st.selectbox("Please select a file to download securely", files)

    if selected_file:
        try:
            encrypted_session_key = encrypt_session_key()

            nonce, tag, ciphertext = server.get_secure_file(
                selected_file,
                encrypted_session_key,
            )

            nonce = b64decode(nonce["data"])
            tag = b64decode(tag["data"])
            ciphertext = b64decode(ciphertext["data"])

            # Decrypt the file content using the session key
            cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
            file_content = cipher_aes.decrypt_and_verify(ciphertext, tag)

            if st.download_button(
                data=file_content,
                file_name=selected_file,
                label="Download file securely",
            ):
                st.success(f"File {selected_file} downloaded successfully!")
                st.write("The contents of the file is:")
                st.text(file_content.decode("utf-8"))

        except FileNotFoundError:
            st.error(f"The file {selected_file} does not exist on the server.")

        except IsADirectoryError:
            st.error("Please enter a filename on the server directory to download.")

        except CommunicationError:
            st.error("The server is not running.")

        except CannotDownloadFile:
            st.error("The file could not be downloaded.")


def app():
    st.title("File Retrieval System")

    # Files on server
    list_files_on_server()

    # Download files without encryption
    download_file_unsecurely()

    # Download files with encryption
    download_file_securely()


if __name__ == "__main__":
    app()
