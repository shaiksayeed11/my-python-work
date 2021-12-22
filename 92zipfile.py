import time
from zipfile import*
import zipfile
f=zipfile("file1.zip","w",ZIP_DEFLATED)
f.write("joshna.txt")
f.write("pick.txt")
f.write("rani.txt")
print()
print("all files are zipped")
time.sleep(1)
print("end of an application")