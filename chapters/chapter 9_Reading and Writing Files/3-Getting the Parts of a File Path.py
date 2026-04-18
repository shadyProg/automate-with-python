from pathlib import Path
import os
#p = Path('C:/Users/ECC/Documents/text.txt')
p = Path('/home/shadyahmed')
'''
that for windows
>>> p = Path('C:/Users/Al/spam.txt')
>>> p.anchor
'C:\\'
>>> p.parent # This is a Path object, not a string.
WindowsPath('C:/Users/Al')
>>> p.name
'spam.txt'
>>> p.stem
'spam'
>>> p.suffix
'.txt'
>>> p.drive
'C:'


'''
#os.chdir('C:/Users/ECC/Documents')

print(Path.cwd())
'''
os.path.dirname(path)
'''

print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)
print(Path.cwd())
# WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')
print(Path.cwd().parents[0])
# WindowsPath('C:/Users/Al/AppData/Local/Programs/Python')
print(Path.cwd().parents[1])
# WindowsPath('C:/Users/Al/AppData/Local/Programs')
Path.cwd()

"""
>>> os.path.dirname(Path.cwd()) 
'C:\\Users\\ECC\\Desktop\\reading\\ReadingComputerScience\\chapters'
!# String
>>> Path.cwd()
WindowsPath('C:/Users/ECC/Desktop/reading/ReadingComputerScience/chapters/chapter 9_Reading and Writing Files')
!# object
"""

"""
>>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.basename(calcFilePath)
'calc.exe'
>>> os.path.dirname(calcFilePath)
'C:\\Windows\\System32'

"""

"""
>>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.split(calcFilePath)
('C:\\Windows\\System32', 'calc.exe')

# that equal to that 

>>> (os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
('C:\\Windows\\System32', 'calc.exe') 
"""
print(os.path.getsize(str(p)))
print(os.listdir(str(p)))

"""

>>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.split(calcFilePath)
('C:\\Windows\\System32', 'calc.exe')
>>> calcFilePath.split(os.sep)
['C:', 'Windows', 'System32', 'calc.exe']
>>> os.sep
'\\'

"""