from pathlib import Path
import os
print(Path.cwd())
currentPath=Path.cwd()
#os.chdir('C:/Windows/System32') # check that i use / not \
os.chdir(str(Path.home()))
print(Path.cwd().is_absolute())
print(Path('egg / follow').is_absolute())

print(Path.cwd()/'egg'/'spam') # don do that , it is poor
print(Path.cwd() / Path('my/relative/path'))
print(Path.home() / Path('my/relative/path'))
os.chdir(currentPath)
print(os.path.abspath(Path('shady', 'room', 'ctf/day')))
print(os.path.abspath('.'))# will return cwd
print(os.path.relpath('C:\\Windows', '.')) ## that very important in hacking to know where are you and your target
print(os.path.relpath(Path.home(), '.'))
