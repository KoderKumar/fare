import os
from subprocess import call
import hashlib
import sys


chosenDir = input(str("Enter folder name you want to lock: "))
hideFileDirName = "Locked Folder.{21EC2020-3AEA-1069-A2DD-08002B30309D}"


os.replace(chosenDir, hideFileDirName)
call(["attrib", "+H", "+S", hideFileDirName])