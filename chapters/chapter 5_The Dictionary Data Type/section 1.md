  

```
spam = {'name': 'Pooka', 'age': 5} 
	if 'color' not in spam:
		 spam['color'] = 'black'
```
طريقة اضيف عنصر جديد 
While they’re still not ordered and have no “first” key-value pair, dictionaries in

Python 3.7 and later will remember the insertion order of their key-value pairs

if you create a sequence value from them. For example, notice the order of

items in the lists made from the eggs and ham dictionaries matches the order in


which they were entered:
```
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}

>>> list(eggs)

['name', 'species', 'age']

>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}

>>> list(ham)

['species', 'age', 'name']
```

The dictionaries are still unordered, as you can’t access items in them

using integer indexes like eggs[0] or ham[2]. You shouldn’t rely on this behavior, as dictionaries in older versions of Python don’t remember the insertion

order of key-value pairs. For example, notice how the list doesn’t match the

insertion order of the dictionary’s key-value pairs when I run this code in

Python 3.5:
```
>>> spam = {}

>>> spam['first key'] = 'value'

>>> spam['second key'] = 'value'

>>> spam['third key'] = 'value'

>>> list(spam)

['first key', 'third key', 'second key']
```

-> defference between The keys(), values(), and items() Methods


  
```

>>> spam = {'color': 'red', 'age': 42}

>>> spam.keys()

dict_keys(['color', 'age'])

>>> list(spam.keys())

['color', 'age']
```
```

>>> spam = {'color': 'red', 'age': 42}

>>> for k, v in spam.items():

... print('Key: ' + k + ' Value: ' + str(v))

Key: age Value: 42

Key: color Value: red
```
فايدة ال items بتطلعلك الاتنين علشان تقدر تستخدمهم 
 Checking Whether a Key or Value Exists in a Dictionary
  ديه شوية عمليات تقدر تستخدمها في methods ديه 


#### get()
the key of the value to retrieve and a fallback value to return if that key does not exist



```
>>> spam = {'name': 'Pooka', 'age': 5}

>>> spam.setdefault('color', 'black')

'black'

>>> spam

{'color': 'black', 'age': 5, 'name': 'Pooka'}

>>> spam.setdefault('color', 'white')

'black'

>>> spam

{'color': 'black', 'age': 5, 'name': 'Pooka'}
```
اخر مثال  في dictunary مش فاهمه 



|         | معنى |
| ------- | ---- |
| tedious |      |



