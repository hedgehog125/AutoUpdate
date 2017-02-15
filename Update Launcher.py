import tkinter as tk
from tkinter import filedialog

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

root = tk.Tk()
root.withdraw()
root.update()
files = root.tk.splitlist(filedialog.askopenfilenames())
fileList = []
for i in range(len(files)):
    path = files[i].split("/")
    for i in range(3):
        del path[0]
    path = "/".join(path)
    fileList.append(path)
files = fileList
    

