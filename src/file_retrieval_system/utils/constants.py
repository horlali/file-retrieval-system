from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
SERVER_FILE_DIR = BASE_DIR / "files" / "server"
CLIENT_FILE_DIR = BASE_DIR / "files" / "client"
KEY_FILE_DIR = BASE_DIR / "src" / "file_retrieval_system" / "keys"
OBJECT_ID = "fileserver"
HOST = "localhost"
PORT = 9090
