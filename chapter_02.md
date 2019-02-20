## Chapter 02

#### copy file and folder

:point_right: using shutil module
```python
import shutil
import os

#shutil provides copy,move , rename and  delete files in your program

shutil.copy('./output.txt', './output_copy.txt')
shutil.copy('./output.txt', './backup')

shutil.copytree('../python101', './backup')



# delete file and folder

os.unlink('/path/file_name')
os.rmdir('/path/dirname')
shutil.rmtree('/path/folder_name')
```

#### walking a directory tree

:point_right: using os module
```python
import os

for  root, subfolders, files in os.walk('./'):
    print (root)
    for subfolder in subfolders:
        print (subfolder)
    for file in files:
        print (file)
```
