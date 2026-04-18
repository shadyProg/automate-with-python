# TODO:
# import libs
# take inputclipboard
# take input key of dic and name of file
import shelve , pyperclip , sys

shelvefile = shelve.open('mcb')

#paste =  pyperclip.paste()

#shelvefile['email']=shady@ , ahmed , ali , hessen
#savelist = []#false
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    #savelist.append(pyperclip.paste())#fasle
    #shelvefile[sys.argv[2]] = savelist #false
    shelvefile[sys.argv[2]] = pyperclip.paste() # that mean new argumnet need to save
elif len(sys.argv) == 2:
    #extract that data of dic 2 
    print(str(list(shelvefile.values())))
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(list(shelvefile.keys()))
    elif sys.argv[1] in shelvefile:
        pyperclip.copy(shelvefile[sys.argv[1]])
shelvefile.close()

# need to test
#py Project/Updatable-Multi-Clipboard.pyw save email
