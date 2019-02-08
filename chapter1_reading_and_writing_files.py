import os
import sys

############################### os module ##############################
######################################################################

current_dir = os.getcwd()
change_dir = os.chdir()

print (f'current_dir : {current_dir}')
print (f'change_dir : {change_dir}')

############# relative and absolut paths ##############################
######################################################################


"""
absolut path = 'always begins whit  the root folder', example: '/home/cgh2/data'

relative path = 'relative to current folder', example : '.'(current), '../'(previous) or '../../(previous, previous)'
"""

############################### make dir##############################
######################################################################

os.makedirs('./mkdir_demo')
change_dir = os.chdir()

################## handling the abs and relative path ###############
#####################################################################

current_dir_path = os.path.abspath('.')
demo_folder_path = os.path.abspath('../mkdir_demo')

print (current_dir_path)
print (demo_folder_path)


file_name = os.path.basename('/home/cgh2/scripts/demo.py')
file_path = os.path.dirname('/home/cgh2/scripts/demo.py')
file_name_from_split, file_path_from_split  =  os.path.split('/home/cgh2/scripts/demo.py')

print (file_name)
print (file_path)
print (file_name_from_split, file_path_from_split)

################## get file size and folder content ###############
#####################################################################

file_size =  os.path.getsize('/Users/cgh2/python101/chaper1_reading_and_writing_files.py')
folder_content = os.listdir('/Users/cgh2/python101')

print (file_size)
print (folder_content)

################## checking path validity ###########################
#####################################################################

answer1 = os.path.exists('/home/cgh2/scripts')
answer2 = s.path.isfile('/home/cgh2/scripts/demo.py')
answer3 = os.path.isdir('/home/cgh2/scripts')

print ('path is existed ? ' + answer1)
print ('file is existed ? ' + answer2)
print ('dir is existed ? ' + answer3)

##################  Read file ########################################
#####################################################################

read_object = open('./LICENSE.txt', 'r')
print (read_object)
content_1 = read_object.read()
content_2 = read_object.readlines()
content_3 = read_object.read().splitlines()
print (content_1)
print (content_2)
print (content_3)

################## write file ########################################
#####################################################################

wf = open('output.txt', 'w')
wf.write('this is the first line\nthis is the secondline\nthis is the third line')
wf.close()


################## others ########################################
#####################################################################


