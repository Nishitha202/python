import os
import zipfile
import pathlib
import sys
dirName=input("enter the directory name you want to backup")
if not os.path.isdir(dirName):
    print("directory",dirName,"doesnt exists")
    sys.exit(0)
curDirectory=pathlib.Path(dirName)
with zipfile.ZipFile("myZip.zip",mode="w")as archive:
    for filepath in curDirectory.rglob("*"):
        archive.write(file_path,arcname=file_path.relativeto(curDirectory))
if os.path.isfile("myZip.zip"):
    print("archive","myZip.zip","created succesfully")
else:
    print('error')

