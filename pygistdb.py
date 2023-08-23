"""# pygistdb
# A Simple Github Gist Database Module"""
import os
import requests
__version__ = 1.0
__name__ = "pygistdb"
content = ""

class gistdb:
    def __init__(self, gistid, token, filename):
        global content
        response = requests.get(f'https://api.github.com/gists/{gistid}')
        gist_data = response.json()
        content = gist_data['files'][filename]['content']
        self.gist_data = response.json()
        self.token = token
        self.gistid = gistid
        self.filename = filename
    def writegist(self, newcontent):
        fcon = self.gist_data
        fcon['files'][self.filename]['content'] = newcontent
        headers = {
            'Authorization': f'token {self.token}',
        }
        requests.patch(
            f'https://api.github.com/gists/{self.gistid}', json=fcon, headers=headers)

def ct():
    with open("temp.db", "w", encoding="utf-8") as f:
        f.write(content)

def dt():
    os.remove("temp.db")


class pydb:
    """
    ## Example:
    ```py
    import pygistdb
    gist = pygistdb.gistdb("gistfileid", "token", "filename")
    db = pygistdb.pydb(gist)
    ```
    """

    def __init__(self, gist):
        self.gist = gist
        self.file = "temp.db"

    def getData(self, key: str):
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            l = f.readlines()
            for i in l:
                if i.find(":") == -1:
                    l.pop(l.index(i))
            il = []
            for i in l:
                il.append(i.split(':')[0])
            if not key in il:
                dt()
                return None
            else:
                for i in l:
                    a = i.split(':')
                    if a[0] == str(key):
                        if len(a) == 2:
                            if a[1] == "{True}\n":
                                dt()
                                return True
                            elif a[1] == "{False}\n":
                                dt()
                                return False
                            elif a[1] == "{None}\n":
                                dt()
                                return None
                            else:
                                dt()
                                return a[1].replace("\n", "")
                        elif len(a) > 2:
                            dt()
                            return ":".join(a[1:]).replace("\n", "")
    def keys(self):
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            keys = []
            lines = f.readlines()
            for i in lines:
                keys.append(i.split(':')[0].replace("\n", ""))
            dt()
            return tuple(keys)
    def values(self):
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            keys = []
            lines = f.readlines()
            for i in lines:
                if len(i.split(':')) < 3:
                    keys.append(i.split(':')[1].replace("\n", ""))
                else:
                    keys.append(":".join(i.split(':')[1:].replace("\n", "")))
            dt()
            return tuple(keys)
    def items(self):
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            items = []
            lines = f.readlines()
            for i in lines:
                if len(i.split(':')) < 3:
                    items.append(
                        [i.split(':')[0], i.split(':')[1].replace("\n", "")])
                else:
                    items.append([i.split(':')[0], ":".join(
                        i.split(':')[1:]).replace("\n", "")])
            dt()
            return tuple(items)
    def addData(self, key, value):
        ct()
        with open(self.file, 'r+', encoding="utf-8") as f:
            valu = value.replace("\n", "")
            keys = []
            lines = f.readlines()
            for i in lines:
                keys.append(i.split(':')[0])
            if not key in keys:
                if lines != []:
                    if lines[len(lines)-1].find('\n') == -1:
                        lines[len(lines)-1] = lines[len(lines)-1]+'\n'
                lines.append(str(key).replace("\n", "").replace(
                    ":", "")+':'+str(valu).replace("\n", "")+'\n')
            f.seek(0)
            f.writelines(lines)
            f.truncate()
        with open(self.file, "r") as f:
            self.gist.writegist(f.read())
    def removeData(self, key):
        ct()
        with open(self.file, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            for i in lines:
                if i.split(':')[0] == str(key):
                    lines.remove(i)
            f.seek(0)
            f.writelines(lines)
            f.truncate()
        with open(self.file, "r") as f:
            self.gist.writegist(f.read())
    def clear(self):
        ct()
        with open(self.file, 'w') as f:
            f.write('clear:1')
    def backUp(self, newfile: str):
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            with open(newfile, 'w') as f:
                f.writelines(lines)
    def setData(self, key, newValue):
        ct()
        with open(self.file, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            for i in lines:
                if i.split(':')[0] == str(key):
                    lines[lines.index(i)] = str(key).replace("\n", "").replace(
                        ":", "")+':'+str(newValue).replace("\n", "")+'\n'
                    f.seek(0)
                    with open(self.file, 'w') as fi:
                        fi.writelines(lines)
        with open(self.file, "r") as f:
            self.gist.writegist(f.read())
    def fileToDICT(self):
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            dictionary = {}
            lines = f.readlines()
            for i in lines:
                if i.find(":") != -1:
                    a = i.split(':')
                    if len(a) == 2:
                        dictionary[a[0]] = a[1].replace("\n", "")
                    if len(a) > 2:
                        dictionary[a[0]] = ":".join(a[1:]).replace("\n", "")
            dt()
            return dictionary
    def dictToFile(self, dictionary: dict):
        ct()
        with open(self.file, 'w', encoding="utf-8") as f:
            lines = []
            for k, v in dictionary.items():
                lines.append("{}:{}\n".format(str(k).replace(
                    "\n", "").replace(":", ""), str(v).replace("\n", "")))
            f.writelines(lines)
        with open(self.file, "r") as f:
            self.gist.writegist(f.read())
    def control(self, key):
        ct()
        """
        ### This Command Checks Whether There Is a Counterpart to the Key
        """
        with open(self.file, 'r', encoding="utf-8") as f:
            l = f.readlines()
            for i in l:
                if i.find(":") == -1:
                    l.pop(l.index(i))
            for i in l:
                if i.split(':')[0] == str(key):
                    dt()
                    return True
            dt()
            return False

class pylist:
    """
    ## Example:
    ```py
    import pygistdb
    gist = pygistdb.gistdb("gistfileid", "token", "filename")
    db=pygistdb.pylist(gist)
    ```
    """
    def __init__(self, gist):
        ct()
        with open("temp.db", "w", encoding="utf-8") as f:
            f.write(content)
        self.gist = gist
        self.file = "temp.db"
    def getData(self, index: int):
        ct()
        with open(self.f, 'r', encoding="utf-8") as f:
            l = f.readlines()
            if len(l)-1 < index:
                dt()
                return None
            else:
                if l[int(index)].replace("\n", "") == "{True}":
                    dt()
                    return True
                elif l[int(index)].replace("\n", "") == "{False}":
                    dt()
                    return False
                elif l[int(index)].replace("\n", "") == "{None}":
                    dt()
                    return None
                else:
                    dt()
                    return l[int(index)].replace("\n", "")
    def listFile(self):
        ct()
        with open(self.f, 'r', encoding="utf-8") as f:
            liste = f.readlines()
            op = []
            for i in liste:
                a = i.replace("\n", "")
                op.append(a)
            dt()
            return op
    def listToFile(self, lst: list):
        ct()
        with open(self.f, 'w', encoding="utf-8") as f:
            liste = []
            for i in lst:
                liste.append(str(i).replace("\n", "")+"\n")
            f.writelines(liste)
        with open(self.file, "r") as f:
            self.gist.writegist(f.read())
    def addData(self, value):
        ct()
        with open(self.f, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            lines.append(str(value).replace("\n", "\\n")+"\n")
            f.seek(0)
            f.writelines(lines)
            f.truncate()
        with open(self.file, "r") as f:
            self.gist.writegist(f.read())
    def setData(self, index: int, value):
        ct()
        with open(self.f, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            lines[int(index)] = str(value).replace("\n", "")+"\n"
            f.seek(0)
            f.writelines(lines)
            f.truncate()
        with open(self.file, "r") as f:
            self.gist.writegist(f.read())
    def removeData(self, index: int):
        ct()
        with open(self.f, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            lines.pop(int(index))
            f.seek(0)
            f.writelines(lines)
            f.truncate()
        with open(self.file, "r") as f:
            self.gist.writegist(f.read())
    def clear(self):
        ct()
        f = open(self.f, 'w', encoding="utf-8")
        f.write("clear:1")
        f.close()
    def lenFile(self):
        ct()
        with open(self.f, 'r', encoding="utf-8") as f:
            liste = f.readlines()
            op = []
            for i in liste:
                a = i.replace("\n", "")
                op.append(a)
            dt()
            return len(op)
    def backUp(self, newfile: str):
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            with open(newfile, 'w') as f:
                f.writelines(lines)
