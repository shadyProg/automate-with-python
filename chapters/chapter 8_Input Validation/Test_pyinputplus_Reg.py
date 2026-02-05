import pyinputplus as pyip
"""
while True:
    response = pyip.inputNum(blockRegexes=[r'[02468]$'])
    print(response)
    """

import pyinputplus as pyip
response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'],
blockRegexes=[r'cat'])
print(response)

