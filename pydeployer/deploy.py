import logging
import os
import ftplib

logger = logging.getLogger(__name__)


class Deploy:
    def __init__(self, ip, user):
        self.ftp = FTP(ip)
        self.ftp.login(user.name, user.password)
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

    def run(self):
        with open("deploy.dat", "r") as dt:
            while True:
                data = dt.readline()
                if data == "":
                    break

                file = data.rstrip() + ".py"
                file_path = os.path.join(dir_path, file)
                ftp.storbinary("STOR " + file, open(file_path, "rb"), 1024)
                print("Send over " + file)

        ftp.close()
        print("Project deployed to server")
