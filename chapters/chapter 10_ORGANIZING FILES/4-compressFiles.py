import zipfile, os , shutil
from pathlib import Path


###############################################################
#'''compresse
newZip = zipfile.ZipFile('1/new.zip', 'a')
newZip.write('1/files/spam_backup/', compress_type=zipfile.ZIP_DEFLATED)
for folderName, subfolders, filenames in os.walk(Path.cwd()/'1/files/spam_backup/'):
   
    for filename in filenames:
       p = '1/files/spam_backup/'+filename 
       newZip.write(p, compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
#'''
###############################################################
#'''read

newZip = zipfile.ZipFile('1/new.zip', 'a') # like open
print(newZip.namelist())


for folderName, subfolders, filenames in os.walk(Path.cwd()/'1/files/spam_backup/'):
   
    for filename in filenames:
       p = '1/files/spam_backup/'+filename 
       spamInfo = newZip.getinfo(p)

print('before compresse :' , spamInfo.file_size)
print('after Compresse  : ' , spamInfo.compress_size)
print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')
newZip.close()
###############################################################
#'''delete


###############################################################

'''
for filename in Path(Path.cwd()/'1/new/1/files/spam_backup').glob('*.txt'):
    os.unlink(filename)
'''
p = Path('./1/new.zip')
#shutil.rmtree(p)
os.unlink(p)



'''
TODO:extract 
w
>>> import zipfile, os
>>> from pathlib import Path
>>> p = Path.home()
>>> exampleZip = zipfile.ZipFile(p / 'example.zip')
 >>> exampleZip.extractall()
>>> exampleZip.close()


exampleZip.extract('spam.txt')

exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')

exampleZip.close()
'''