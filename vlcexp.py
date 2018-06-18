#Grotesque silly unnecessary hack
#Must work on alternative that directly reads and modifies .ini file [use context wrapper]

import os

from shutil import copyfile

os.chdir("C:\\Users\\XXXXX\\AppData\\Roaming\\vlc")

os.remove('vlc-qt-interface.ini')

os.chdir("C:\\Users\\XXXXXX\\AppData\\Roaming\\vlc\\backupinterfaceini")

copyfile('backupinterfaceini' , "C:\\Users\\XXXXXX\\AppData\\Roaming\\vlc")


