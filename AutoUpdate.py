# Released under cc licence: https://creativecommons.org/
# Made by @hedgehog125 on github.com and scratch.mit.edu
import urllib.request, os, shutil, ast
from time import sleep
database = "unknown"
FileList = ""
new = []
Updates = ""
FileList = ""
def Get_Web_Info(Address, decode=True):
    url = Address
    response = urllib.request.urlopen(url)
    data = response.read()      # a `bytes` object
    if not decode:
        return data
    text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    return (text)

def Open_File(File,Write,Text):
    if Write:
        f = open(File,'w')
        f.write(Text)
    else:
        f = open(File)
        text = f.readlines()
        f.close()
        return (text)
    f.close()


def GetFileList(messageReceiver):
    global FileList
    global updates
    messageReceiver("Retrieving file list...")
    FileList = Get_Web_Info(database + "Files.txt")
    FileList = ast.literal_eval(FileList)
    
def CheckForUpdates(messageReceiver):
    global Updates
    global Latest
    global Downloaded
    global new
    messageReceiver("Checking for updates...")
    Updates = Get_Web_Info(database + "Versions.txt")
    Updates = Updates.split(",")
    Latest = Updates[len(Updates)-1]
    Downloaded = Open_File("Versions.txt",False,"")[0]
    if len(Downloaded) > 0:
        Downloaded = ast.literal_eval(Downloaded)
    else:
        Downloaded = []
    new = []
    if Downloaded != Updates:
        for i in range(len(Updates) - len(Downloaded)):
            new.append(Updates[i + len(Downloaded)])
    if len(new) > 0:
        if len(new) == 1:
            messageReceiver("1 update found!")
        else:
            messageReceiver(str(len(new)) + " updates found!")
    else:
        messageReceiver("No updates found.")

def GetFiles(messageReceiver):
    messageReceiver("Downloading files...")
    for v in new:
        ver = str(v)
        if ver in FileList:
            for i in range(len(FileList[ver])):
                if FileList[ver][i][0]:
                    if FileList[ver][i][3]:
                        g = urllib.request.urlopen(FileList[ver][i][2])
                        with open("Assets/" + FileList[ver][i][1], 'b+w') as f:
                            f.write(g.read())
                    else:
                        Open_File("Assets/" + FileList[ver][i][1],True,FileList[ver][i][2])                        
                else:
                    try:
                        os.makedirs("Assets/" + FileList[ver][i][1])
                    except:
                        messageReceiver("Tampered files detected.")
                        messageReceiver("Restoring...")
                        messageReceiver("")
                        shutil.rmtree("Assets")
                        sleep(0.5)
                        os.makedirs("Assets")
                        return True

    if len(new) == 1:
        messageReceiver("Update installed!")
    else:
        messageReceiver("Updates installed!")
    messageReceiver("Updating installed file...")
    Open_File("Versions.txt",True,str(Updates))
    messageReceiver("Done!")
    return False

def init(messageReceiver = print):
    if (database == "unknown"):
        return
    CheckForUpdates(messageReceiver)
    sleep(0.5)
    if len(new) > 0:
        GetFileList(messageReceiver)
        if GetFiles(messageReceiver):
            init(messageReceiver)
