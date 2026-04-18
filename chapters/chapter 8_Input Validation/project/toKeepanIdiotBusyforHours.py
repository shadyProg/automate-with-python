import pyinputplus as pyip
try:
    response = pyip.inputYesNo(prompt='Want to know how to keep an idiot busy for hours? \n' , timeout=3)
    print(response)

    if response == 'yes' :
        print("hello let`s start to know.")
    elif response == 'no':
        print(" sorry for You.")
    else:
        print ('oh way ')
except:
    print('catch')