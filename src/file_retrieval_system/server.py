import logging
import os
from base64 import b64decode

import Pyro4
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

from utils.constants import HOST, OBJECT_ID, PORT, SERVER_FILE_DIR

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


@Pyro4.expose
class FileServer(object):
    directory = SERVER_FILE_DIR

    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    def get_public_key(self):
        return self.public_key

    def list_files(self):
        files = []
        for filename in os.listdir(self.directory):
            path = os.path.join(self.directory, filename)
            if os.path.isfile(path):
                files.append(filename)
        return files

    def get_file(self, filename):
        with open(os.path.join(self.directory, filename), "rb") as f:
            return f.read()

    def get_secure_file(self, filename, encrypted_session_key):
        cipher_rsa = PKCS1_OAEP.new(self.key)
        decoded_encrypted_session_key = b64decode(encrypted_session_key["data"])
        session_key = cipher_rsa.decrypt(decoded_encrypted_session_key)

        with open(os.path.join(self.directory, filename), "rb") as f:
            file_content = f.read()

            # Encrypt the file content using the session key
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(file_content)

            return cipher_aes.nonce, tag, ciphertext


daemon = Pyro4.Daemon(host=HOST, port=PORT)
uri = daemon.register(FileServer(), objectId=OBJECT_ID)
logger.info(f"File Retrieval Server Ready. Object URI: {uri}")
daemon.requestLoop()
