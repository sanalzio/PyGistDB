"""# pygistdb
# A Simple Github Gist Database Module"""
import os
import requests
__version__ = 1.1
__name__ = "pygistdb"
content = ""

class congist:
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
    f=open("temp.pydb", "w", encoding="utf-8")
    f.write(content)
    f.close()

def dt(g,f):
    g.writegist(f.read())
    f.close()
    os.remove("temp.pydb")

class pydb:
    """
    ## Example:
    ```py
    import pygistdb
    pygistdb.congist("gistfileid", "token", "filename")
    db = pygistdb.pydb()
    ```
    """
    def __init__(self, gist):
        self.g=gist
        self.file = "temp.pydb"
    def getData(self, key):
        key=str(key)
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            l = f.readlines()
            for i in l:
                if i.find(":")==-1:
                    l.pop(l.index(i))
            il=[]
            for i in l:
                il.append(i.split(':')[0])
            if not key in il:
                f.seek(0)
                dt(self.g, f)
                return None
            else:
                for i in l:
                    a=i.split(':')
                    if a[0]==str(key):
                        if len(a) == 2:
                            if a[1]=="{True}\n":
                                f.seek(0)
                                dt(self.g, f)
                                return True
                            elif a[1]=="{False}\n":
                                f.seek(0)
                                dt(self.g, f)
                                return False
                            elif a[1]=="{None}\n":
                                f.seek(0)
                                dt(self.g, f)
                                return None
                            else:
                                f.seek(0)
                                dt(self.g, f)
                                return a[1].replace("\n", "").replace("\\n", "\n")
                        elif len(a)>2:
                            f.seek(0)
                            dt(self.g, f)
                            return ":".join(a[1:]).replace("\n", "")
    def keys(self):
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            keys=[]
            lines = f.readlines()
            for i in lines:
                keys.append(i.split(':')[0].replace("\n", "").replace("\\n", "\n"))
            f.seek(0)
            dt(self.g, f)
            return tuple(keys)
    def values(self):
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            keys=[]
            lines = f.readlines()
            for i in lines:
                if len(i.split(':')) < 3:
                    keys.append(i.split(':')[1].replace("\n", "").replace("\\n", "\n"))
                else:
                    keys.append(":".join(i.split(':')[1:]).replace("\n", "").replace("\\n", "\n"))
            f.seek(0)
            dt(self.g, f)
            return tuple(keys)
    def items(self):
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            items=[]
            lines = f.readlines()
            for i in lines:
                if len(i.split(':')) < 3:
                    items.append([i.split(':')[0].replace("\\n", "\n"), i.split(':')[1].replace("\n", "").replace("\\n", "\n")])
                else:
                    items.append([i.split(':')[0].replace("\\n", "\n"), ":".join(i.split(':')[1:]).replace("\n", "").replace("\\n", "\n")])
            f.seek(0)
            dt(self.g, f)
            return tuple(items)
    def addData(self, key, value):
        key=str(key)
        ct()
        with open(self.file, 'r+', encoding="utf-8") as f:
            valu=value
            if value==True:
                valu="{True}"
            if value==False:
                valu="{False}"
            if value==None:
                valu="{None}"
            else:
                valu=value.replace("\n","\\n")
            keys=[]
            lines = f.readlines()
            for i in lines:
                keys.append(i.split(':')[0])
            if not key in keys:
                if lines!=[]:
                    if lines[len(lines)-1].find('\n') == -1:
                        lines[len(lines)-1]=lines[len(lines)-1]+'\n'
                lines.append(str(key).replace("\n", "\\n").replace(":", "")+':'+str(valu).replace("\n", "\\n")+'\n')
            f.seek(0)
            f.writelines(lines)
            f.truncate()
            f.seek(0)
            dt(self.g, f)
    def removeData(self, key):
        key=str(key)
        ct()
        with open(self.file, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            for i in lines:
                if i.split(':')[0]==str(key):
                    lines.remove(i)
            f.seek(0)
            f.writelines(lines)
            f.truncate()
            f.seek(0)
            dt(self.g, f)
    def clear(self):
        ct()
        with open(self.file, 'w') as f:
            f.write('None:None\n')
        with open(self.file, 'r') as f:
            dt(self.g, f)
    def backUp(self, newfile:str):
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            with open(newfile+".pydb", 'w') as f:
                f.writelines(lines)
        with open(self.file, 'r', encoding="utf-8") as f:
            f.seek(0)
            dt(self.g, f)
    def setData(self, key, newValue):
        key=str(key)
        if newValue==True:
            valu="{True}"
        if newValue==False:
            valu="{False}"
        if newValue==None:
            valu="{None}"
        valu = str(newValue).replace("\n","\\n")
        ct()
        with open(self.file, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            for i in lines:
                if i.split(':')[0]==str(key):
                    lines[lines.index(i)]=str(key).replace("\n", "").replace(":", "")+':'+valu+'\n'
                    f.seek(0)
                    ct()
                    with open(self.file, 'w') as fi:
                        fi.writelines(lines)
            f.seek(0)
            dt(self.g, f)
    def fileToDICT(self):
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            dictionary={}
            lines= f.readlines()
            for i in lines:
                if i.find(":")!=-1:
                    a=i.split(':')
                    if len(a)==2:
                        if a[0]!="None":
                            dictionary[a[0]]=a[1].replace("\n", "")
                    if len(a)>2:
                        if a[0]!="None":
                            dictionary[a[0]]=":".join(a[1:]).replace("\n", "")
            f.seek(0)
            dt(self.g, f)
            return dictionary
    def dictToFILE(self, dictionary:dict):
        ct()
        dictionary=dictionary
        dictionary["None"]="None"
        with open(self.file, 'w', encoding="utf-8") as f:
            lines=[]
            for k,v in dictionary.items():
                lines.append("{}:{}\n".format(str(k).replace("\n", "").replace(":", ""),str(v).replace("\n","")))
            f.writelines(lines)
        with open(self.file, 'r', encoding="utf-8") as f:
            dt(self.g, f)
    def control(self, key):
        key=str(key)
        """
        ### This Command Checks Whether There Is a Counterpart to the Key
        """
        ct()
        with open(self.file, 'r', encoding="utf-8") as f:
            l= f.readlines()
            for i in l:
                if i.find(":")== -1:
                    l.pop(l.index(i))
            for i in l:
                if i.split(':')[0]==str(key):
                    f.seek(0)
                    dt(self.g, f)
                    return True
            return False

class pylist:
    """
    ## Example:
    ```py
    import pygistdb
    pygistdb.congist("gistfileid", "token", "filename")
    db=pygistdb.pylist()
    ```
    """
    def __init__(self, gist):
        self.g=gist
        self.f="temp.pydb"
    def getData(self, index:int):
        ct()
        with open(self.f, 'r', encoding="utf-8") as f:
            l=f.readlines()
            if "NoneVariable\n" in l:
                l.pop(l.index("NoneVariable\n"))
            if len(l)-1 < index:
                f.seek(0)
                dt(self.g, f)
                return None
            else:
                if l[int(index)].replace("\n", "") == "{True}":
                    f.seek(0)
                    dt(self.g, f)
                    return True
                elif l[int(index)].replace("\n", "") == "{False}":
                    f.seek(0)
                    dt(self.g, f)
                    return False
                elif l[int(index)].replace("\n", "") == "{None}":
                    f.seek(0)
                    dt(self.g, f)
                    return None
                else:
                    f.seek(0)
                    dt(self.g, f)
                    return l[int(index)].replace("\n", "").replace("\\n", "\n")
    def listFile(self):
        ct()
        with open(self.f, 'r', encoding="utf-8") as f:
            liste=f.readlines()
            if "NoneVariable\n" in liste:
                liste.pop(liste.index("NoneVariable\n"))
            op = []
            for i in liste:
                if i.replace("\n","")=="{True}":
                    op.append(True)
                    continue
                if i.replace("\n","")=="{False}":
                    op.append(False)
                    continue
                if i.replace("\n","")=="{None}":
                    op.append(None)
                    continue
                a=i.replace("\n","").replace("\\n", "\n")
                op.append(a)
                f.seek(0)
            dt(self.g, f)
            return op
    def listToFILE(self, lst):
        ct()
        with open(self.f, 'w', encoding="utf-8") as f:
            liste= list(["NoneVariable\n"])
            for i in lst:
                if i==True and i!=1:
                    liste.append("{True}\n")
                    continue
                if i==False:
                    liste.append("{False}\n")
                    continue
                if i==None:
                    liste.append("{None}\n")
                    continue
                liste.append(str(i).replace("\n","\\n")+"\n")
            f.writelines(liste)
        with open(self.f, 'r', encoding="utf-8") as f:
            dt(self.g, f)
    def addData(self, value):
        ct()
        with open(self.f, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            if value==True:
                lines.append("{True}\n")
            if value==False:
                lines.append("{False}\n")
            if value==None:
                lines.append("{None}\n")
            else:
                lines.append(str(value).replace("\n","\\n")+"\n")
            f.seek(0)
            f.writelines(lines)
            f.truncate()
            f.seek(0)
            dt(self.g, f)
    def setData(self, index:int, value):
        ct()
        with open(self.f, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            if "NoneVariable\n" in lines:
                lines.pop("NoneVariable\n")
            if value==True:
                lines[int(index)]="{True}\n"
            if value==False:
                lines[int(index)]="{False}\n"
            if value==None:
                lines[int(index)]="{None}\n"
            else:
                lines[int(index)]=str(value).replace("\n","\\n")+"\n"
            f.seek(0)
            f.writelines(lines)
            f.truncate()
            f.seek(0)
            dt(self.g, f)
    def removeData(self, index:int):
        ct()
        with open(self.f, 'r+', encoding="utf-8") as f:
            lines=f.readlines()
            lines.pop(int(index))
            f.seek(0)
            f.writelines(lines)
            f.truncate()
            f.seek(0)
            dt(self.g, f)
    def clear(self):
        ct()
        f= open(self.f, 'w', encoding="utf-8")
        f.write("NoneVariable\n")
        f.close()
        f= open(self.f, 'r', encoding="utf-8")
        f.seek(0)
        dt(self.g, f)
    def backUp(self, newfile:str):
        ct()
        with open(self.f, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            with open(newfile+".pydb", 'w') as f:
                f.writelines(lines)
        with open(self.f, 'r', encoding="utf-8") as f:
            f.seek(0)
            dt(self.g, f)
    def lenFile(self):
        ct()
        with open(self.f, 'r', encoding="utf-8") as f:
            liste=f.readlines()
            if "NoneVariable\n" in liste:
                liste.pop(liste.index("NoneVariable\n"))
            op = []
            for i in liste:
                a=i.replace("\n","")
                op.append(a)
                f.seek(0)
            dt(self.g, f)
            return len(op)
    def index(self, value):
        if not value==True or not value==False or not value==None:
            if str(value) in self.listFile():
                return self.listFile().index(str(value))
            else:
                return -1
        else:
            if value in self.listFile():
                return self.listFile().index(value)
            else:
                return -1
