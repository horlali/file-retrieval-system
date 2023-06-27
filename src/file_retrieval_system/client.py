import Pyro4
import streamlit as st

uri = st.text_input("Enter Pyro4 server URI")
new_file = st.text_input("Enter filename to download")

if st.button("Download"):
    file_server = Pyro4.Proxy(uri)
    file_data = file_server.get_file(new_file)

    print(type(file_data))
    print(file_data["data"])

    encode_data = file_data["data"].encode("utf-8")

    print("===========", f"{file_data['data'].encode('utf-8')}")

    with open("hello.py", "wb") as f:
        f.write(encode_data)

    st.success(f"File {new_file} downloaded successfully!")
