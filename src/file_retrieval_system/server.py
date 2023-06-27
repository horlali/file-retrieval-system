import logging
import os

import Pyro4

from file_retrieval_system.utils.constants import (
    HOST,
    OBJECT_ID,
    PORT,
    SERVER_FILE_LOCATION,
)

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


@Pyro4.expose
class FileServer(object):
    directory = SERVER_FILE_LOCATION

    def list_files(self):
        files = []
        print(self.directory)
        for filename in os.listdir(self.directory):
            path = os.path.join(self.directory, filename)
            if os.path.isfile(path):
                files.append(filename)
        return files

    def get_file(self, filename):
        with open(os.path.join(self.directory, filename), "rb") as f:
            return f.read()


daemon = Pyro4.Daemon(host=HOST, port=PORT)
uri = daemon.register(FileServer(), objectId=OBJECT_ID)
logger.info(f"File Retrieval Server Ready. Object URI: {uri}")
daemon.requestLoop()
