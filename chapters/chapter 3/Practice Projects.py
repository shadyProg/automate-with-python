import sys
def collatz(number):
    if number%2 == 0 :
        return number
    else:
        return  3 * number + 1
    
try:
    while True :
        
            user_input = int(input("enter int number \n "))

            print("after function " +str(collatz(user_input)) )
except ValueError:
    print("please enter integer number")
    
except KeyboardInterrupt :
    print("good bye")
    sys.exit()


