## Dealing with string

:point_right: single '' and double ""

```
print ('this is my dog')
print ('this is my sister's dog')
print ("this is my sister's dog")
```

:point_right: escape character
```
print ('this is my  sister\'s dog)

print ('\'')
print ('\"')
print ('\t')
print ('\n')
print ('\\')
```

:point_right: raw string
```
print (r'this is my  sister\'s dog')
print (r'this is my  sister's dog')

```

:point_right: multiline string
```
'''this is a multimiline string  example,
so i put 3 lines here for just
demo this function'''
```

:point_right: multiline comments
```
"""this  is a multiline comment example,
so i  put 3 lines  here for just
demo this function"""
```
:point_right: index and  slicing string
```
![index_string](index_string.png)
word ='hello world!'
print (word[0])
print (word[0:5])
print (word[-1])
print (word[::2])
```
:point_right: in and not in operator with string
```
'hello' in 'hello world!'

'world' in 'hello  world!'

'Hello' in 'hello world!'

'money'not in 'hello world!'
```

:point_right: the upper(), lower(), isupper(), islower() string method
```
print ('abc'.upper())
print ('ABC'.lower())
print ('abc'.upper().lower())

```

:point_right: startswith, endswith string method
```
'hello world'.strtswith('hello')
'hello world'.strtswith('he')
'hello world'.endswith('world')
'hello world'.endswith('rld')

```

:point_right: join and  split string  method
```
','.join(['a', 'b', 'c'])
'-'.join(['a', 'b', 'c'])
'ttt'.join(['a', 'b', 'c'])

'my name is cgh2'.split('')
'my name is cgh2'.split('is')

```

:point_right: strip(),  rstrip(), lstrip()
```
spam = '   hello    '
print (spam.strip())
print (spam.rstrip())
print (spam.lstrip())

```

:point_right: copying and pasting  with the pyperclip module

```
"""
The pyperclip module has copy() and paste() functions that can send text 
to and receive text from your computer’s clipboard. Sending the output 
of your program to the clipboard will make it easy to paste it to an email,
word processor, or some other software.
"""
import pyperclip
pyperclip.copy('hello world!')
pyperclip.paste()
```


