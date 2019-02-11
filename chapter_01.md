## chapter 1

reading and  writing files

:point_right:using `os.getcwd()` to get current directory , `os.change_dir()` to change the directory you want, `os.mkdir() to make a new directory`



```python
import os

current_dir = os.getcwd('/home/cgh2/demo.txt')
change_dir = os.chdir('/home/cgh3')
new_dir = os.mkdir('/home/cgh4')

print (f'current_dir : {current_dir}')
print (f'change_dir : {change_dir}')
print (f'new_dir:{new_dir}')
```



:point_right:  absolute path vs relative path, using `os.path.abspth('demo.txt')`. to get the path of the dmeo.txt, using `os.path.abspath('../demo')` to get the path of the upper folder

```python
import os

dmeo_txt_path = os.path.abspath('demo.txt')
demo_folder_path = os.path.abspath('../')

print (demo_txt_path)
print (demo_folder_path)

file_name = os.path.basename('/home/cgh2/demo/demo.txt')
file_path = os.path.dirname('/home/cgh2/demo/demo.txt')
file_name_from_split,  file_path_from_split = os.path.split('/home/cgh2/demo/demo.txt')

print (file_name)
print (file_path)
print (file_name_from_split, file_path_from_split)
```



:point_right:  using `os.path.getsize()`. to get the size of the file, `os.listdir()` to get the Folder content

```python
import os

file_size = os.path.getsize('/home/cgh2/demo/demo.txt')
folder_content = os.listdir('/home/cgh2/demo')

print (file_size)
print (folder_content)
```



:point_right:   checking path validity

```python
import os

answer_1 = os.path.exists('/home/cgh2/demo/demo.txt')
answer_2 = os.path.isfile('/home/cgh2/demo/demo.txt')
answer_3 = os.path.isdir('/home/cgh2/demo/')

print (f'path is existed : {answer_1}')
print (f'file is existed : {answer_2}')
print (f'folder is existed : {answer_3}')
```



:point_right:   reading and writing

```python  
import os

file_object = open("/home/cgh2/demo/demo.txt", "r")
file_content_1 = file_object.read()
file_content_2 = file_object.readlines()
file_content_3 = file_object.read().splitlines()

print (file_content_1)
print (file_content_2)
print (file_content_3)

wf = open('/home/cgh2/demo/demo_write.txt', 'w')
wf.write('testing for writing file\noh my god\nhello, world')
wf.close()#very important
```