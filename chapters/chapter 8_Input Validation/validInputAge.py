import pyinputplus as pyinput
while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break
print(f'Your age is {age}.')
"""
_for try behavior_
name = 'a'
name2 = 'asd'
name = int(name)
name2 = int(name2)
print(name,name2)
"""
