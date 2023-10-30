>>> rollnumbers = ['anagh','srilakshmi','vishalrs','vijayeshwar']
>>> rollnumbers.append('vishals')
>>> print(rollnumbers)
['anagh', 'srilakshmi', 'vishalrs', 'vijayeshwar', 'vishals']
>>> rollnumbers.insert(0,'nandana')
>>> print(rollnumbers)
['nandana', 'anagh', 'srilakshmi', 'vishalrs', 'vijayeshwar', 'vishals']
>>> rollnumbers.append("chandan")
>>> print(rollnumbers)
['nandana', 'anagh', 'srilakshmi', 'vishalrs', 'vijayeshwar', 'vishals', 'chandan']
>>> rollnumbers.pop('chandan')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> rollnumbers.remove('chandan')
>>> print(rollnumbers)
['nandana', 'anagh', 'srilakshmi', 'vishalrs', 'vijayeshwar', 'vishals']
>>> rollnumbers.sort(reverse = True)
>>> print(rollnumbers)
['vishals', 'vishalrs', 'vijayeshwar', 'srilakshmi', 'nandana', 'anagh']
>>> rollnumbers = rollnumber
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rollnumber' is not defined. Did you mean: 'rollnumbers'?
>>> rollnumber = rollnumbers
>>> rollnumber
['vishals', 'vishalrs', 'vijayeshwar', 'srilakshmi', 'nandana', 'anagh']
>>> rollnumbers = batch.copy()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'batch' is not defined
>>> rollnumbers = rollnumber.copy()
>>> rollnumber
['vishals', 'vishalrs', 'vijayeshwar', 'srilakshmi', 'nandana', 'anagh']
>>> rollnumbers.clear()
>>> rollnumbers
[]
>>> rollnumber
['vishals', 'vishalrs', 'vijayeshwar', 'srilakshmi', 'nandana', 'anagh']
>>> del rollnumbers
>>> rollnumbers
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rollnumbers' is not defined. Did you mean: 'rollnumber'?
>>>