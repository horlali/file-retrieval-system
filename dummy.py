import os

from file_retrieval_system.utils import constants, encryptions

encryptions.create_keys()
publicKey, privateKey = encryptions.load_keys()
with open(os.path.join(constants.SERVER_FILE_DIR, "data.csv"), "rb") as f:
    file_content = f.read()

    ciphertext = encryptions.encrypt(file_content, privateKey)
    print("cipher text", ciphertext)

    signature = encryptions.sign(ciphertext, publicKey)
    print("signature", signature)

    print(ciphertext)
    print(signature)
