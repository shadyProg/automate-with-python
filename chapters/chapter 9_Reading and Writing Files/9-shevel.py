import shelve
shelvefile = shelve.open('mydic')

cats = {'sandy','mishmish','osman'}
shelvefile['Listcat']=cats
print(shelvefile['Listcat'])
shelvefile.close()
#print(shelvefile['Listcat']) !error
shelfile = shelve.open('mydic')
print(shelfile['Listcat'])
print(list(shelfile.values()))
print(list(shelfile.keys()))
shelfile.close()

shelfile = shelve.open('targets') # name of file cant be Path

shelfile['google'] = ['mail.google.com', 'drive.google.com']

shelfile.close()

