import os
from pathlib import Path
# walk in all the tree
for folderName, subfolders, filenames in os.walk(Path.home()/'Public'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
print('')   