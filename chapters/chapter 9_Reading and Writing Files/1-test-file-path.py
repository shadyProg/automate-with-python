from pathlib import Path
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\Al', filename))
    
    print(str(Path(r'C:\Users\Al', filename)))
print(str(Path('spam', 'bacon', 'eggs')))
print(Path('spam') / 'bacon')

"""
So while Path(r'spam\eggs') refers to two separate folders (or
a file eggs in a folder spam) on Windows
, so prefer use r with path.
\\بدل يعني ما تكتب 
"""



