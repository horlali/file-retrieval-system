import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

SERVER_FILE_DIR = BASE_DIR / "files" / "server"
CLIENT_FILE_DIR = BASE_DIR / "files" / "client"

OBJECT_ID = os.getenv("OBJECT_ID")
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
