import re

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
print(mo1.group(0))
print(
    ''' Heroes: Batman and Tina Fey
    dont fiar that only try print multiple group with parentheses
'''
    )
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

"""


"""