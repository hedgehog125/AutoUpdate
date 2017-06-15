Welcome to auto update.py!

To get started import "AutoUpdate.py"...

import AutoUpdate
Or from a directory:

import AutoUpdate/AutoUpdate

Next you must specify the database... e.g:

https://raw.githubusercontent.com/hedgehog125/AutoUpdateExample

If you want to run locally you can use file:///

So add to your code:

AutoUpdate.database = [Put your database here]

Then run init()...

AutoUpdate.init()
This will check for updates and download new versions.
You can also pass a function through it and you can use it to edit the messages e.g:

def displayMessage(mess):
  print("AutoUpdate says... " + mess)
  
AutoUpdate.init(displayMessage)
  
Or maybe you don't want to display messages...

def youCanCallThisWhateverYouLike(mess):
  return
  
AutoUpdate.init(youCanCallThisWhateverYouLike)

Check Auto-Update/Test.py for an example.

If you want to make a database for this check out https://github.com/hedgehog125/Auto-Update-Database.py
