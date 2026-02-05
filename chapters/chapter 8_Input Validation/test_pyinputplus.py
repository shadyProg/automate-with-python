import pyinputplus as pyip
userInput=pyip.inputInt(prompt='Enter your age: ', min=5)
# min is used to set the minimum value that can be accepted. In this case, it will only accept integers greater than or equal to 5.
print(f'Your age is {userInput}.')

response = pyip.inputNum('Enter num: ')
print(response)
response = pyip.inputNum(blank=True)

print(response)


