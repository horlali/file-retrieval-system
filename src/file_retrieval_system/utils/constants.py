from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
SERVER_FILE_LOCATION = BASE_DIR / "files" / "server"
CLIENT_FILE_LOCATION = BASE_DIR / "files" / "client"
OBJECT_ID = "fileserver"
HOST = "localhost"
PORT = 9090
