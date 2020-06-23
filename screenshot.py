import pyperclip
from subprocess import PIPE, Popen
import datetime
import time
import os

cwd = os.getcwd()

try:
    fh = open(cwd+"\\scrshtNum.txt", "x")
    fh.close()
    fh = open(cwd+"\\scrshtNum.txt", "w")
    fh.write("0")
    fh.close()
except Exception as e:
    print(e)
            
fh = open(cwd+"\\scrshtNum.txt", "r")
i = int(fh.read())
fh.close()

i += 1

p = Popen(["nircmd.exe","savescreenshot","C:\\Users\\rocco\\Desktop\\screenshot"+str(i)+".png"], shell=True)
p.wait()
Popen(["file2clip.exe", "C:\\Users\\rocco\\Desktop\\screenshot"+str(i)+".png"], shell=True)

fh = open(cwd+"\\scrshtNum.txt", "w")
fh.write(str(i))
fh.close()