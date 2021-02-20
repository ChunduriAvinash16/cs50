>>> import re
>>> s="Hello , Good morning"
>>> p1=","
>>> re.match(p1,s)
>>> if re.match(p1,s):
...     print("match")
... else:
...     print("Not match")
... 
Not match
>>> print(re.match(p1.s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 's'
>>> print(re.match(p1,s))
None
>>> p1="Hello"
>>> print(re.match(p1,s))
<re.Match object; span=(0, 5), match='Hello'>
>>> re.match(p1,s)
<re.Match object; span=(0, 5), match='Hello'>
>>> print("match") if re.match(p1,s) else print("not match")
match
>>> print("match") if re.match(p1,s,re.I) else print("not match")
match
>>> p1="hello"
>>> print("match") if re.match(p1,s,re.I) else print("not match")
match
>>> print("match") if re.match(p1,s) else print("not match")
not match
>>> p1="h ello'
  File "<stdin>", line 1
    p1="h ello'
              ^
SyntaxError: EOL while scanning string literal
>>> p1="h ello"
>>> print("match") if re.match(p1,s) else print("not match")
not match
>>> print("match") if re.match(p1,s,re.I or re.X) else print("not match")
not match
>>> p1
'h ello'
>>> print("match") if re.match(p1,s,re.X) else print("not match")
not match
>>> ps="h ello"
>>> print("match") if re.match(p1,s,re.X) else print("not match")
not match
>>> print("match") if re.match(p1,ps,re.X) else print("not match")
not match
>>> p1
'h ello'
>>> ps
'h ello'
>>> print("match") if re.match(p1,ps) else print("not match")
match
>>> print("match") if re.match(p1,ps,re.X) else print("not match")
not match
>>> s
'Hello , Good morning'
>>> p1="Good"
>>> print("match") if re.search(p1,s) else print("not match")
match
>>> print("match") if re.match(p1,s) else print("not match")
not match
>>> p1="good"
>>> print("match") if re.search(p1,s) else print("not match")
not match
>>> print("match") if re.search(p1,s,re.I) else print("not match")
match
>>> print("match") if re.search(p1,s) else print("not match")
not match
>>> p1
'good'
>>> p1="Morning"
>>> re.sub(p1,"Aviansh",s,re.I)
'Hello , Good morning'
>>> re.sub(p1,"Aviansh",s)
'Hello , Good morning'
>>> p1="morning"
>>> re.sub(p1,"Aviansh",s)
'Hello , Good Aviansh'
>>> s="hello hello hello hello"
>>> p1="morning"
>>> p1="hello"
>>> re.sub(p1,"Avinash",s)
'Avinash Avinash Avinash Avinash'
>>> re.sub(p1,"Avinash",s,max=2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sub() got an unexpected keyword argument 'max'
>>> re.sub(p1,"Avinash",s)
'Avinash Avinash Avinash Avinash'
>>> re.sub(p1,"Avinash",s,=2)
  File "<stdin>", line 1
    re.sub(p1,"Avinash",s,=2)
