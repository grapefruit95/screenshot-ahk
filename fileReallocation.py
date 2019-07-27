import sqlite3
import os
from distutils.dir_util import copy_tree
import shutil
import winshell
#reads db which has format [name, path, move, copy, delete, movedst, sys]
def readDB():
    dbConnection = sqlite3.connect("pathsToCheck.db")
    cursor = dbConnection.cursor()
    cursor = cursor.execute("SELECT * FROM DATA")
    allEntries = cursor.fetchall()

    for entry in allEntries:
        if entry[6]:
            #checking sys files (only Recycle Bin so far)
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
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