import pyperclip
from subprocess import PIPE, Popen
import datetime
import time
fh = open("D:\\rocco\\Documents\\repo\\scrshtNum.txt", "r")
i = int(fh.read())
fh.close()

i += 1

p = Popen(["nircmd.exe","savescreenshot","C:\\Users\\rocco\\Desktop\\screenshot"+str(i)+".png"], shell=True)
p.wait()
Popen(["file2clip.exe", "C:\\Users\\rocco\\Desktop\\screenshot"+str(i)+".png"], shell=True)

fh = open("D:\\rocco\\Documents\\repo\\scrshtNum.txt", "w")
fh.write(str(i))
fh.close()