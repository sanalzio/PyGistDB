<h1 style="color:#fe8a71;">PyGistDB</h1>

A primitive module enabling the use of your GitHub Gist as a database.

<h1 style="color:#fe8a71;">Updates</h1>

- <b style="color:#fdf498">I discovered a file writing issue in the module and fixed it</b>
- <b style="color:#fdf498">pygist class name changed to congist</b>
- Now the module allows data with newline(\n) characters.
- Added index function to pylist class. [Go!](https://github.com/sanalzio/PyGistDB/blob/main/README.md#Get-variable-index)
- Added lenFile function to pylist class. [Go!](https://github.com/sanalzio/PyGistDB/blob/main/README.md#Get-list-lenght)

<h1 style="color:#fe8a71;">Dictionary</h1>
<h1 style="color:#f6cd61;">import example:</h1>

```py
import pygistdb
gist = pygistdb.congist("gistfileid", "token", "filename")
db = pygistdb.pydb(gist)
```

<h1 style="color:#f6cd61;">add data</h1>

old file:
```
var1:123
```
code:
```py
db.addData("var2","456")
```
new file:
```
var1:123
var2:456
```

<h1 style="color:#f6cd61;">get data</h1>

file content:
```
var1:123
varTrue:{True}
varFalse:{False}
varNone:{None}
```
code:
```py
print(db.getData("var1"))
print(db.getData("varTrue"))
print(db.getData("varFlas"))
print(db.getData("varNone"))
```
output:
```
123
True
Flase
None
```

<h1 style="color:#f6cd61;">remove data</h1>

old file:
```
var1:123
var2:456
```
code:
```py
db.removeData("var2")
```
new file:
```
var1:123
```

<h1 style="color:#f6cd61;">clear file</h1>

old file:
```
var1:123
var2:456
```
code:
```py
db.clear()
```
new file:
(empty)

<h1 style="color:#f6cd61;">backup data</h1>

gist content:
```
var1:123
var2:456
```
code:
```py
db.backUp("backup1.db")
```
backup1.db file content:
```
var1:123
var2:456
```

<h1 style="color:#f6cd61;">set data</h1>

old content:
```
var1:123
var2:456
```
code:
```py
db.setData("var2", "789")
```
new content:
```
var1:123
var2:789
```

<h1 style="color:#f6cd61;">Retrieve the data in </h1>
dictionary format
gist content:
```
var1:123
var2:789
```
code:
```py
content = db.fileToDICT()
print(content)
```
output:
```
{'var1':'123', 'var2':'789'}
```

<h1 style="color:#f6cd61;">Dictionary to gist</h1>

code:
```py
mydict = {'var':'Hello', 'varint':123}
db.dictToFile(mydict)
```
new gist content:
```
var:Hello
varint:123
```

<h1 style="color:#f6cd61;">Control data</h1>

gist content:
```
var:Hello
```
code:
```
print(db.control("var"))
print(db.control("varint"))
```
output:
```
True
False
```

<h1 style="color:#f6cd61;">Get datas</h1>

gist content:
```
var:Hello
varint:123
```
code:
```py
print(db.keys())
print(db.values())
print(db.items())
```
output:
```
("var", "varint")
("Hello", "123")
(("var", "Hello"), ("varint", "123"))
```

<h1 style="color:#fe8a71;">List</h1>
<h1 style="color:#f6cd61;">import example:</h1>

```py
import pygistdb
gist = pygistdb.congist("gistfileid", "token", "filename")
db = pygistdb.pylist(gist)
```

<h1 style="color:#f6cd61;">add data</h1>

old file:
```
123
```
code:
```py
db.addData(456)
```
new file:
```
123
456
```

<h1 style="color:#f6cd61;">get data</h1>

file content:
```
123
{True}
{False}
{None}
```
code:
```py
print(db.getData(0))
print(db.getData(1))
print(db.getData(2))
print(db.getData(3))
```
output:
```
123
True
Flase
None
```

<h1 style="color:#f6cd61;">remove data</h1>

old file:
```
123
456
```
code:
```py
db.removeData(1)
```
new file:
```
123
```

<h1 style="color:#f6cd61;">clear file</h1>

old file:
```
123
456
```
code:
```py
db.clear()
```
new file:
(empty)

<h1 style="color:#f6cd61;">backup data</h1>

gist content:
```
123
456
```
code:
```py
db.backUp("backup1.db")
```
backup1.db file content:
```
123
456
```

<h1 style="color:#f6cd61;">set data</h1>

old content:
```
123
456
```
code:
```py
db.setData(1, 789)
```
new content:
```
123
789
```

<h1 style="color:#f6cd61;">Retrieve the data in list </h1>

gist content:
```
Hello
123
```
code:
```py
content = db.listFile()
print(content)
```
output:
```
["Hello", "123"]
```

<h1 style="color:#f6cd61;">List to gist</h1>

code:
```py
mylist = ["Hello", "I'm fine thank you"]
db.listToFile(mylist)
```
new gist content:
```
Hello
I'm fine thank you
```

<h1 style="color:#f6cd61;">Get list lenght</h1>

gist content:
```
Hello
123
```
code:
```py
print(db.lenFile())
```
output:
```
2
```

<h1 style="color:#f6cd61;">Get variable index</h1>

gist content:
```
Hello
123
```
code:
```py
print(db.index("Hello"))
print(db.index("Hello, World"))
```
output:
```
-1
```
