![mycat](./mycat.jpg)

## chapter 1

#### some things you  should know before starting learn pytohn

- **python2  or python 3**, which one?
- **virtualenv** : what and why?
- **python module** : must know and must learn to use
- **bpython** : realtime coding demo
- **github** : must know and ~~must learn to use~~ 
- **codind tools** : depends on you
  - [visual studio code](https://code.visualstudio.com/)
  - [pycharm](https://www.jetbrains.com/pycharm/)
  - [sublime text](https://www.sublimetext.com/)
  - [notepad++](https://notepad-plus-plus.org/zh/)
  - VIM

## chapter 2

#### reading and  writing files

###### :point_right:using `os.getcwd()` to get curretn directory , `os.change_dir()` to change the directory you want, `os.mkdir() to make a new directory`



```python
import os

current_dir = os.getcwd()
change_dir = os.chdir()
new_dir = os.mkdir()

print (f'current_dir : {current_dir}')
print (f'change_dir : {change_dir}')
print (f'new_dir:{new_dir}')
```



:point_right:absolute path vs relative path : using `os.path.abspth('demo.txt')`. to get the path of the dmeo.txt, using `os.path.abspath('../demo')` to get the path of the upper folder

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



:point_right:using `os.path.getsize()`. to get the size of the file, `os.listdir()` to get the. Folder content

```python
import os

file_size = os.path.getsize('/home/cgh2/demo/demo.txt')
folder_content = os.listdir('/home/cgh2/demo')

print (file_size)
print (folder_content)
```



:point_right: checking path validity

```python
import os

answer_1 = os.path.exists('/home/cgh2/demo/demo.txt')
answer_2 = os.path.isfile('/home/cgh2/demo/demo.txt')
answer_3 = os.path.isdir('/home/cgh2/demo/')

print (f'path is existed : {answer_1}')
print (f'file is existed : {answer_2}')
print (f'folder is existed : {answer_3}')
```



:point_right:using `open()` to open file for  reading and.  writing  

```python  
import os

### for reading
file_object = open('/home/cgh2/demo/demo.txt', 'r')

print (file_object)

file_content_1 = file_object.read()
file_content_2 = file_object.readlines()
file_content_3 = file_object.read().splitlines()

print (file_content_1)
print (file_content_2)
print (file_content_3)

### for writing
wf = open('/home/cgh2/demo/demo_write.txt', 'w')
wf.write('this is my first time writing python\n not funny at all\n byebye')
wf.close() # very import
```

