import re , pyperclip
def mask_phone_and_email(text):
    # Regex for phone numbers (simple US format)
    phone_regex = re.compile(r'(\d{3}-\d{3}-\d{4})')

    """
        phoneRegex = re.compile(r'''(
        --snip--
        # Create email regex.
        emailRegex = re.compile(r'''(
         [a-zA-Z0-9._%+-]+ # username
         @ # @ symbol
         [a-zA-Z0-9.-]+ # domain name
        (\.[a-zA-Z]{2,4}) # dot-something
        )''', re.VERBOSE)
    what writer codeing
    """
    # Regex for email addresses
    # email_regex = re.compile(r'(.*@.*\..{2,3})') not eff

    email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+    # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
    )''', re.VERBOSE)

    whatFound= []

    # Find phone numbers
    phone_matches = phone_regex.findall(text)
    whatFound.extend(phone_matches) # add to list in right way

    # Find email addresses
    email_matches = email_regex.findall(text)
    whatFound.extend(email_matches)

    return whatFound
input()
text = str(pyperclip.paste())
objectsFound = mask_phone_and_email(text)
print(objectsFound)
#matches = []
"""
for groups in phoneRegex.findall(text):
phoneNum = '-'.join([groups[1], groups[3], groups[5]])
if groups[8] != '':
phoneNum += ' x' + groups[8]
matches.append(phoneNum)
for groups in emailRegex.findall(text):
matches.append(groups[0)
shadyAhmed@gmai.com
123-123-1233
"""