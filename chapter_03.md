## function

#### define function

:point_right:function example
```
def hello():
    print ("hello world!")
```

:point_right: function with parameter

```
def hello(name):
    print (f"hello, {name}")
```
:point_right: function must with return

```function without return
def add(a, b):
    print (a+b)

add(3, 5)

```
:point_right: return
```function with return
def add(a, b):
    return (a+b)

c = add(3, 5)

print (c)

```
:point_right: return None
```function with default return None
def add(a, b):
    print (a+b)
    return()

add(3, 5)

```
:point_right: arguments, keyword arguments and print

```arguments
def add(a, b):
    print (a + b)

add()
```
``` keyword arguments
print ("cat", "dog", "pig")

print ("cat", "dog", "pig", sep=',')
```

#### local and global scope

:point_right:local variables cannot be used in global scope
```
def spam():
    eggs = 1234

print eggs
```
:point_right: local scope cannot use variabales in other local scope
```
def spam():
    eggs = 1234
    bacon()
    print (eggs)


def bacon():
    ham = 4567
    eggs = 0

spam()
```


