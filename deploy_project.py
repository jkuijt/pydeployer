import os
import ftplib
from ftplib import FTP

ftp = FTP('<ip>')
ftp.login("<name>", "<password>")
dir_path = os.path.dirname(os.path.realpath(__file__))

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