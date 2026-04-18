from pathlib import Path
import os 
size = os.path.getsize('')
sizekg = size/1024 
sizemg = sizekg/1024 
sizegg = sizemg/1024 
print('Size in bytes : ' , str(size) )
print('Size in KB : ' + str(size/1024)  )
print('Size in MB : ' + str(float(size/(1024**2))) )
print('Size in GB : ' + str(float(size/1024**3) ))
print('Size in bytes : ' , str(size) )
print('Size in KB : ' + str(sizekg)  )
print('Size in MB : ' + str(float(sizemg)) )
print('Size in GB : ' + str(float(sizegg) ))

print(os.listdir(Path.cwd()))
print(os.path.dirname(Path.cwd()))# os.path.dirname its take abspath
print(Path.cwd())


