from pathlib import Path
p = Path('spam.txt')
p.write_text("""hello sir ,
            Iam shady . that way to understand new technology.""")
print(p.read_text())
helloContent = p.open()
print(helloContent.read())
print(helloContent.close())
baconFile = open('bacon.txt', 'w') # path or str of path 
print(baconFile.write('Hello, world!\n'))
baconFile = open('bacon.txt', 'a')
print(baconFile.write('Bacon is not a vegetable.'))
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
""" 
sonnet = open(p)
print(sonnet.read())        # بعد ما قريت الملف بقا فاضي 
print(sonnet.readlines())
"""
"""
cause pointer 
use with it is better or read_text 
"""

with open(p )as sonnet: # with return pointer to first after finish
    print('1' , sonnet.read()) 
with open(p) as sonnet:
    print('2' ,sonnet.readline(5))
with open(p) as sonnet:
    print('3 ' ,sonnet.readlines())    


"""
There are three steps to reading or writing
files in Python:
1. Call the open() function to return a File object.
2. Call the read() or write() method on the File object.
3. Close the file by calling the close() method on the File object.
We’ll go over these steps in the following sections.
"""
'''
it is make file in cwd
'''