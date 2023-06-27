import os
from base64 import b64decode

import Pyro4
import streamlit as st

from file_retrieval_system.utils.constants import CLIENT_FILE_DIR, HOST, OBJECT_ID, PORT
from file_retrieval_system.utils.encryptions import decrypt, load_keys

URI = f"PYRO:{OBJECT_ID}@{HOST}:{PORT}"
server = Pyro4.Proxy(URI)


def app():
    st.title("File Retrieval System")

    st.header("Files on server")
    st.write("The following files are available on the server:")
    files = server.list_files()

    if not files:
        st.write("No files found.")
    else:
        for filename in files:
            st.markdown(f"- {filename}")

    st.header("Unencrypted file exchange")
    st.header("retrieve files")
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
            st.text(data_str)

        except FileNotFoundError:
            st.error(f"The file {filename} does not exist on the server.")

        except IsADirectoryError:
            st.error("Please enter a filename on the server directory to download.")

    st.header("Encrypted file exchange")
    st.header("retrieve files")
    filename = st.text_input("Enter secure filename to download")

    if st.button("Download2"):
        try:
            file_contents = server.get_secure_file(filename)

            if file_contents:
                _, privateKey = load_keys()
                decrypted_data = decrypt(file_contents["data"], privateKey)
                data_bytes = b64decode(decrypted_data)
                data_str = data_bytes.decode()

            with open(os.path.join(CLIENT_FILE_DIR, filename), "wb") as f:
                f.write(data_str.encode())

            st.success(f"File {filename} downloaded successfully!")
            st.text(data_str)

        except FileNotFoundError:
            st.error(f"The file {filename} does not exist on the server.")

        except IsADirectoryError:
            st.error("Please enter a filename on the server directory to download.")


if __name__ == "__main__":
    app()
