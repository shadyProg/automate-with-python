
import re

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())



greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())



