## Dictionary

:point_right: the dictionary data type {}

```
>>> mydict = {'size': 'fat', 'color':'blue', 'favorite' : 'eating'}
```

:point_right: dict's key and value

```
>>> mydict['size']

>>> mydict['color']

>>> spam = {123:'onetwothree', 456:{'fourfivesix'}}

>>> spam[123]

>>> spam[456]

```

:point_right: dictionary vs list

```
# unlike list items in dict are unorder

>>> mylist_1 = [1, 3, 7]

>>> mylist_2 = [1, 7, 3]

>>> mylist_1 == myslit_2 # should be false

>>> mydict_1 = {1:'one', 2:'two', 3:'three'}

>>> mydict_2 = {1:'one', 3:'three', 2:'two'}

>>> mydict_1 == mydict_2 #  should be true

```

:point_right: keys(), values(), and items() methods

```
>>> mydict_1 = {1:'one', 2:'two', 3:'three'}

>>> for v in mydict_1.values():
        print (v)

>>> for  k in mydict_1.keys():
        print (k)

>>> for i in mydict_1.items():
        print (i)

>>> for i, j in mydict_1.items():
        print (i, j)

```
:point_right: the get() method

```
>>> mydict_1 = {1:'one', 2:'two', 3:'three'}

>>> mydict_1.get(1, 'nothing')

>>> mydict_1.get(4, 'nothing')

```
:point_right: setdefault() method

```
# original
>>> mydict_1 = {1:'one', 2:'two', 3:'three'}

if 4 not in mydict_1.keys():
        mydict_1[4] = 'four'

# using setdefault method
>>> mydict_1.setdefault(4, 'four')

```
:point_right: pretty printing

```
>>> import pprint

>>> message = 'if this waat you like, just do it.'

>>> count  = {}

>>> for char in message:
        count.setdefault(char, 0)
        count[char] = count[char] + 1
    print (count)

>>> for char in message:
        count.setdefault(char, 0)
        count[char] = count[char] + 1
    pprint (count)
```

