import os.path
import sys
fname=input("enter the filename")
if not os.path.isfile(fname):
    print("the file",fname,"doesn't exists")
    sys.exit(0)
infile=open(fname,"r")
linelist=infile.readlines()
for i in range(10):
    print(i+1,":",linelist[i])
word=input("enter the word")
cnt=0
for line in linelist:
    cnt+=line.count(word)
print("the word",word,"appears",cnt," times in file")