import sys
while True:
        line = input()
        print("You entered:", line)
        if line.lower() == 'exit':
            print("Exiting the program.")
            sys.exit()
        else:
            continue
