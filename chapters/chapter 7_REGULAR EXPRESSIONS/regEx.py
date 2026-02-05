import re
def find_email_addresses(text):
    """
    This function takes a string input and returns a list of all email addresses found in the string.
    An email address is defined as a sequence of characters that includes an '@' symbol and a domain.
    """
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}')
    sh = email_pattern.search(text)
    return sh.group() if sh else None

print("Please contact us at shadyahmed@gmail.com  for further information : \n -> " , end="")
print(find_email_addresses("Please contact us at shadyahmed@gmail.com  for further information."))
print("does not contain email : \n -> " , end="")
print(find_email_addresses("does not contain email"))


