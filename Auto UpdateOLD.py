import urllib.request
#database = "www.nicoc.uk/Python_Projects/AutoUpdate/Downloads/database/"
database = "file:///Users/nico/Documents/My%20Website/Python_Projects/Auto_Update/Downloads/database/"
FileList = ""
def Get_Web_Info(Address):
    url = Address
    response = urllib.request.urlopen(url)
    data = response.read()      # a `bytes` object
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
def getFiles():
    global FileList
    FileList = Get_Web_Info(database + "Files.txt")
    FileList.split(",")
def CheckForUpdates():
    Updates = Get_Web_Info(database + "Versions.txt")
    Updates.split(",")
    Latest = Updates[len(Updates)-1]
    Downloaded = Open_File("../Versions.txt")
    
getFiles()
