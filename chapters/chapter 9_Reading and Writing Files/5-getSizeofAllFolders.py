import os 
totalSize = 0
#print(os.listdir('C:\\Windows\\System32'))
for filename in os.listdir('/home'):
    totalSize = totalSize + os.path.getsize(os.path.join('/home', filename))
print('total SizeData in GB :  ',totalSize/1024**2,' MB')


'''
totalSize = 0
for filename in os.listdir('/home/shadyahmed'):
    totalSize = totalSize + os.path.getsize(os.path.join('/home/shadyahmed', filename))
#       totalSize = totalSize + os.path.getsize(Path('/home/shadyahmed',filename))
print(totalSize)

getsize work in single file so you should do loop

'''