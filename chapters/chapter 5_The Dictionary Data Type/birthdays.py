person = {'ali':'feb 2 ', 'yehia':'mars 3' , 'shady':' jul 4'}
while True:
    name = input('enter name :\t')
    if name in person:
        print ("name is "+ name + "\tbirthday is " +person[name] )
    elif name == '':
        break
    else :
        print ('not found')

data_base=list(person)
print(data_base)
