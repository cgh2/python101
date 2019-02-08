# -*- coding: utf-8 -*-
import shutil
import os

######################## shutil module  ######################################
#############################################################################
#shutil provides copy,move , rename and  delete files in your program



######################## copy file and folder ######################################
#############################################################################

shutil.copy('./output.txt', './output_copy.txt')
shutil.copy('./output.txt', './backup')

shutil.copytree('../python101', './backup')


######################## delete file /folder######################################
#############################################################################

os.unlink('/path/file_name')
os.rmdir('/path/dirname')
shutil.rmtree('/path/folder_name')

######################## walking a directory tree######################################
#############################################################################
import os
for  root, subfolders, files in os.walk('./'):
    print (root)
    for subfolder in subfolders:
        print (subfolder)
    for file in files:
        print (file)
