# PyGistDB 1.3
A primitive module enabling the use of your GitHub Gist as a database.

![logo](image.svg)

# Updates
- **I discovered a file writing issue in the module and fixed it**
- **pygist class name changed to congist**
- **Changed pygistdb.congist usage** [Go!](https://github.com/sanalzio/PyGistDB/blob/main/README.md#import-example)
- Now the module allows data with newline(\n) characters.
- Added index function to pylist class. [Go!](https://github.com/sanalzio/PyGistDB/blob/main/README.md#Get-variable-index)
- Added lenFile function to pylist class. [Go!](https://github.com/sanalzio/PyGistDB/blob/main/README.md#Get-list-lenght)
- Litle write gist fix.
- Read fix.
- Memory usage optimization.

# Requirements
- Python 3
- requests
  - `pip install requests`
- os

# Dictionary
## import example:
```py
import pygistdb
gist = pygistdb.congist("gistfileid", "filename", "token")
db = pygistdb.pydb(gist)
```

## add data
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

## get data
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

## remove data
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

## clear file
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

## backup data
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

## set data
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

## Retrieve the data in dictionary format
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

## Dictionary to gist
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

## Control data
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

## Get datas
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

# List
## import example:
```py
import pygistdb
gist = pygistdb.congist("gistfileid", "filename", "token")
db = pygistdb.pylist(gist)
```

## add data
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

## get data
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

## remove data
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

## clear file
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

## backup data
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

## set data
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

## Retrieve the data in list format
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

## List to gist
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

## Get list lenght
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

## Get variable index
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
