import sqlite3
import os
from distutils.dir_util import copy_tree
import shutil
import subprocess
from subprocess import Popen, PIPE
import time
#reads db which has format [name, path, move, copy, delete, movedst, sys]
def readDB():
    dbConnection = sqlite3.connect("pathsToCheck.db")
    cursor = dbConnection.cursor()
    cursor = cursor.execute("SELECT * FROM DATA")
    allEntries = cursor.fetchall()

    for entry in allEntries:
        if entry[6]:
            #checking sys files (only Recycle Bin so far)
            Popen(["nircmd.exe", "emptybin"])
        elif entry[4]:
            os.remove(entry[1])
            os.mkdir(entry[1])
        elif entry[3]:
            shutil.move(entry[1], entry[5])
        elif entry[2]:
            shutil.move(entry[1], entry[5])
            os.remove(entry[1])
        else:
            print("invalid DB entry"+entry[0])

            

readDB()