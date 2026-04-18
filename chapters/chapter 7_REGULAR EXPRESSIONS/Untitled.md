Here are the answers to the practice questions for Chapter 7, followed by the code and logic for the chapter’s main project.

### Answers to Chapter 7 Practice Questions

1. **`re.compile()`** is the function that creates Regex objects.
2. **Raw strings** are used so that backslashes (`\`) do not have to be escaped.
3. The **`search()`** method returns **Match objects**.
4. You call the Match object’s **`group()`** method to retrieve the actual strings that match the pattern.
5. In the regex `r'(\d\d\d)-(\d\d\d-\d\d\d\d)'`, **group 0** covers the entire match, **group 1** covers the first set of parentheses (the area code), and **group 2** covers the second set of parentheses.
6. You must **escape them with a backslash**: `\.`, `\(`, and `\)`.
7. If the regex has **no groups**, it returns a list of strings. If it **has groups**, it returns a list of tuples of strings.
8. The `|` character signifies **“either, or”** matching between two groups.
9. The `?` character can signify either **optional matching** (zero or one of the preceding group) or be used to signify **non-greedy matching**.
10. The **`+` matches one or more**, while the **`*` matches zero or more**.
11. The **`{3}`** matches exactly three instances of the preceding group. The **`{3,5}`** matches between three and five instances.
12. These shorthand classes match a single **digit** (`\d`), **word** (`\w`), or **space** (`\s`) character, respectively.
13. These shorthand classes match a single character that is **NOT** a digit (`\D`), word (`\W`), or space (`\S`) character, respectively.
14. The **`.*` is a greedy match** (takes the longest string), while **`.*?` is a non-greedy match** (takes the shortest string).
15. The syntax is either **`[0-9a-z]`** or **`[a-z0-9]`**.
16. You pass **`re.I`** or **`re.IGNORECASE`** as the second argument to `re.compile()`.
17. The `.` character normally matches any character **except the newline**. If **`re.DOTALL`** is passed as the second argument, it will also match newline characters.
18. It will return the string **`'X drummers, X pipers, five rings, X hens'`**.
19. It allows you to **add whitespace and comments** to the regex string to make it more readable.
20. **`re.compile(r'^\d{1,3}(,\d{3})*$')`**.
21. **`re.compile(r'[A-Z][a-z]*\sWatanabe')`**.
22. **`re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)`**.

---

### Required Project: Phone Number and Email Address Extractor

The main project for Chapter 7 is a script that automatically finds all phone numbers and email addresses in the text currently on your system clipboard and replaces the clipboard content with a clean list of the matches found.

#### **Program Logic**

1. **Get the text off the clipboard** using the `pyperclip` module.
2. **Create a Regex for Phone Numbers**: This pattern includes optional area codes, various separators (hyphen, period, space), and optional extensions.
3. **Create a Regex for Email Addresses**: This pattern matches standard username formats, the `@` symbol, and domain names.
4. **Find all matches**: Use the `findall()` method to retrieve every occurrence in the text.
5. **Format and Paste**: Join the matches into a single newline-separated string and copy it back to the clipboard.

#### **Project Source Code**

```
#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# Create phone regex.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups, groups, groups])
    if groups != '':
        phoneNum += ' x' + groups
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups)

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
```

### Practice Projects

The chapter also assigns three additional practice tasks:

- **Date Detection**: A regex to detect dates in `DD/MM/YYYY` format and logic to verify if they are valid (e.g., checking for leap years).
- **Strong Password Detection**: A function using multiple regex patterns to ensure a password is at least 8 characters long, has both upper and lowercase, and at least one digit.
- **Regex Version of strip()**: A function that replicates the `strip()` method's behavior using regex instead of built-in string methods.