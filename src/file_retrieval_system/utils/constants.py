import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

KEY_FILE_DIR = BASE_DIR / "src" / "file_retrieval_system" / "keys"
SERVER_FILE_DIR = BASE_DIR / "files" / "server"

Path(KEY_FILE_DIR).mkdir(parents=True, exist_ok=True)
Path(SERVER_FILE_DIR).mkdir(parents=True, exist_ok=True)

OBJECT_ID = os.getenv("OBJECT_ID")
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
