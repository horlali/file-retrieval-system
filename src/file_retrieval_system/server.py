import glob
import os

import Pyro4


@Pyro4.expose
class FileServer(object):
    directory = ""

    def list_files(self):
        files = []
        for filename in os.listdir(self.directory):
            path = os.path.join(self.directory, filename)
            if os.path.isfile(path):
                files.append(filename)
        return files

    def get_file(self, filename):
        with open(filename, "rb") as f:
            return f.read()


daemon = Pyro4.Daemon()
uri = daemon.register(FileServer)
print("Ready. Object uri =", uri)
daemon.requestLoop()
