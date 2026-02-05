# Executive Summary

Chapter 7, **"Pattern Matching with Regular Expressions,"** focuses on moving beyond basic string searching (like `Ctrl-F`) to using **regular expressions (regex)** to identify complex text patterns. The chapter teaches how to automate the identification of data like phone numbers and email addresses, making code much shorter and more powerful than using manual string checking.

---

# Deep-Dive Content: Pattern Matching with Regular Expressions

## 1. Patterns Without Regular Expressions

Before learning regex, the author demonstrates why manual string checking is inefficient.

### 1.1 Manual Pattern Checking

- **The Problem**: Checking if a string is a phone number using standard methods requires many lines of `if` statements and loops to check every digit and hyphen individually.
- **Complexity**: Manual functions (like `isPhoneNumber()`) are "bloated" and can only find one specific format. If the format changes slightly (e.g., adding an area code in parentheses), the code fails.

## 2. Patterns with Regular Expressions

Regex provides a "magic wand" to identify specific formats using specialized codes.

### 2.1 The `re` Module and Regex Objects

- **Importing**: You must first use `import re` to access regex functions.
- **Creation**: Use `re.compile()` to create a **Regex object**. This object holds the pattern you want to find.
- **Raw Strings**: The author recommends using raw strings (e.g., `r'\d\d\d'`) to avoid escaping backslashes manually.

### 2.2 Finding and Matching

- **The `search()` Method**: This method looks for the first occurrence of a pattern in a string.
- **Match Objects**: If a match is found, `search()` returns a **Match object**. If not, it returns `None`.
- **The `group()` Method**: Call this on a Match object to return the actual text that was found.
- **Example Code**:
    
    ```
    import re
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phoneNumRegex.search('My number is 415-555-4242.')
    print('Phone number found: ' + mo.group()) # Output: 415-555-4242
    ```

```
 phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') 
  mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1) 
>>>  '415'
 mo.group(2)
>>>  '555-4242' 
 mo.group(0) 
>>>  '415-555-4242' 
 mo.group()
>>> '415-555-4242'
```


## 3. Advanced Pattern Grouping

Regex allows you to break matches into smaller parts.

### 3.1 Grouping with Parentheses

- **Structure**: Parentheses `()` if not found  create groups within a pattern. `group(1)` returns _the first set_, `group(2)` the second, and `group(0)` (or no argument) returns the whole match.
- **Multiple Groups**: Use `groups()` (plural) to retrieve a tuple containing all matched groups at once.

```
 phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') 
  mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1) 
>>>  '415'
 mo.group(2)
>>>  '555-4242' 
 mo.group(0) 
>>>  '415-555-4242' 
 mo.group()
>>> '415-555-4242'
```


```
 mo.groups() 
 >>> ('415', '555-4242') 
 areaCode, mainNumber = mo.groups() 
 print(areaCode)
 >>> 415 
 print(mainNumber)
 >>> 555-4242
```

_Since_  `mo.groups()` returns a tuple of multiple values, you can use the multiple-assignment trick to assign each value to a separate variable, as in the `previous areaCode, mainNumber = mo.groups() line.`
### 3.2 The Pipe Operator (`|`)

- **Usage**: The pipe acts like an "OR" statement, matching one of many possible expressions (e.g., `r'Batman|Tina Fey'`).
- **Prefix Matching**: You can match multiple words with the same prefix using parentheses: `r'Bat(man|mobile|copter)'`.
- with group is return what can see first  cant return more than one match
```
 heroRegex = re.compile (r'Batman|Tina Fey')

 mo1 = heroRegex.search('Batman and Tina Fey')

 mo1.group()

 >>> 'Batman'

 mo2 = heroRegex.search('Tina Fey and Batman')

 mo2.group()

>>> 'Tina Fey'

```


## 4. Repetition and Optional Matching

Special characters define how many times a pattern should appear.

### 4.1 Quantifiers

- **Question Mark (`?`)**: Matches **zero or one** of the preceding group (makes it optional).
- **Star (`*`)**: Matches **zero or more** occurrences.
- **Plus (`+`)**: Matches **one or more** (at least one is required).
- **Braces (`{n,m}`)**: Matches a specific range of repetitions (e.g., `{3,5}` matches 3, 4, or 5 repetitions) , can be `{n}`



### 4.2 Greedy vs. Non-greedy Matching

- **Greedy**: Python's default; matches the **longest** possible string.
- **Non-greedy**: Adding a `?` after braces (e.g., `{3,5}?`) tells Python to match the **shortest** possible string.

## 5. Character Classes and Boundaries

Shorthand codes help you match categories of characters.

### 5.1 Common Shorthands

- **`\d`**: Any numeric digit.
- **`\w`**: Any letter, digit, or underscore.
- **`\s`**: Any space, tab, or newline character.
- **Negative Classes**: Uppercase versions (`\D`, `\W`, `\S`) match anything **except** those categories.
- **Custom Classes**: Defined with `[]` (e.g., `[aeiouAEIOU]` to match vowels). Use `^` inside brackets for a negative class (e.g., `[^aeiou]` to match non-vowels).

### 5.2 Position Anchors

- **Caret (`^`)**: Indicates the match must occur at the **beginning** of the text.
- **Dollar Sign (`$`)**: Indicates the match must occur at the **end** of the text.
- **Mnemonic**: The author uses "Carrots cost dollars" to remember that `^` comes first and `$` comes last.
```
 wholeStringIsNum = re.compile(r'^\d+$')

 wholeStringIsNum.search('1234567890')

<re.Match object; span=(0, 10), match='1234567890'>

wholeStringIsNum.search('12345xyz67890') == None

>>> True

wholeStringIsNum.search('12 34567890') == None

>>> True
```

### 5.3 Dot 

- `. (or dot) `: The character in a regular expression is called a wildcard and will match any character except for a newline

```

 atRegex = re.compile(r'.at')

 atRegex.findall('The cat in the hat sat on the flat mat.')

>>> ['cat', 'hat', 'sat', 'lat', 'mat']

```
#### _Matching Everything with Dot-Star_

```
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') 
 mo = nameRegex.search('First Name: Al Last Name: Sweigart') 
 mo.group(1) 
 >>> 'Al' 
 mo.group(2)
 >>> 'Sweigart'
```

- match with greedy
```
 nongreedyRegex = re.compile(r'<.*?>')

 mo = nongreedyRegex.search('<To serve man> for dinner.>')

 mo.group()

>>> '<To serve man>'

 greedyRegex = re.compile(r'<.*>')

 mo = greedyRegex.search('<To serve man> for dinner.>')

 mo.group()

>>> '<To serve man> for dinner.>'

```
_HINT_
Why didn't it stop at the first `>`?

A crucial question 👌 The short answer:

> Because `.*` **isn't required to stop at the first `>`**

> It's only required to leave space for `>` at the end **and that's it**

Meaning:

- Any `>` in the middle is **perfectly fine**

- The important thing is that at the end, there's always one `>` to close the regex
#### _Matching Newlines with the Dot Character_

- By passing re.DOTALL as the second argument to re.compile()


```


 noNewlineRegex = re.compile('.*')

 noNewlineRegex.search('Serve the public trust.\nProtect the innocent.

\nUphold the law.').group()

>>> 'Serve the public trust.'

 newlineRegex = re.compile('.*', re.DOTALL)

 newlineRegex.search('Serve the public trust.\nProtect the innocent.

\nUphold the law.').group()

>>> 'Serve the public trust.\nProtect the innocent.\nUphold the law.' 

```

## 6. Global Search and Substitution

Methods for finding every match or changing text.

### 6.1 The `findall()` Method

- **Difference from `search()`**: While `search()` returns the first match, `findall()` returns a _list_ of every match in the entire string and doesn\`t need to  search.
- **Return Format**: If the regex has no groups, it returns a list of strings; if it has groups, it returns a list of tuples.
```

 phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups

 phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

>>> ['415-555-9999', '212-555-0000']

```

![[Screenshot (85).png]]
### 6.2 The `sub()` Method

- **Function**: Finds matches and **substitutes** them with new text.
- **Group Backreferences**: You can use `\1`, `\2`, etc., in the replacement string to use the matched text itself in the substitution.
- `\1` return first it save by self 

```

 namesRegex = re.compile(r'Agent \w+') 
 namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
>>> 'CENSORED gave the secret documents to CENSORED.'

```

```
 agentNamesRegex = re.compile(r'Agent (\w)\w*')

 agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent

Eve knew Agent Bob was a double agent.')

>>> A**** told C**** that E**** knew B**** was a double agent.'
```
## 7. Complex Regex Management

Large regexes can be hard to read; Python provides tools to organize them.

### 7.1 Case-Insensitive Matching

- **Method**: Pass `re.IGNORECASE` (or `re.I`) as the second argument to `re.compile()`.

```

 robocop = re.compile(r'robocop', re.I)

 robocop.search('RoboCop is part man, part machine, all cop.').group()

>>> 'RoboCop'

 robocop.search('ROBOCOP protects the innocent.').group()

>>> 'ROBOCOP'

 robocop.search('Al, why does your programming book talk about robocop so much?').group()

>>> 'robocop

```


### 7.2 Verbose Mode

- **Method**: Pass `re.VERBOSE` to ignore whitespace and comments inside the regex string, allowing you to spread it over multiple lines using triple quotes.

```

phoneRegex = re.compile(r'''(

 (\d{3}|\(\d{3}\))? # area code

 (\s|-|\.)? # separator

 \d{3} # first 3 digits

 (\s|-|\.) # separator

 \d{4} # last

(\s*(ext|x|ext.)\s*\d{2,5})? # extension

 )''', re.VERBOSE)

```

### 7.3Verbose Mode



---

# ⚠️ Important Notes & Warnings

- **Escaping Special Characters**: Characters like `. ^ $ * + ? { } [ ] \ | ( )` have special meanings. To match them as literal text, you **must** escape them with a backslash (e.g., `\.` or `\?`).
- **The "re" Import Trap**: Forgetting `import re` is a common mistake that leads to a `NameError`.
- **Greedy Default**: Be aware that regexes will take the longest match by default, which can lead to bugs if you only need a specific section.
- **The professional summary:**
	'r' is not for regex.
	'r' is for Python itself.
	It says:

	>"Don't interpret backslashes, leave them for regex."


•    The ? matches zero or one of the preceding group.

•    The * matches zero or more of the preceding group.

•    The + matches one or more of the preceding group.

•    The {n} matches exactly n of the preceding group.

•    The {n,} matches n or more of the preceding group.

•    The {,m} matches 0 to m of the preceding group.

•    The {n,m} matches at least n and at most m of the preceding group.

•    {n,m}? or *? or +? performs a non-greedy match of the preceding group.

•    ^spam means the string must begin with spam.

•    spam$ means the string must end with spam.

•    The . matches any character, except newline characters.

•    \d, \w, and \s match a digit, word, or space character, respectively.

•    \D, \W, and \S match anything except a digit, word, or space character,

respectively.

•    [abc] matches any character between the brackets (such as a, b, or c).

•    [^abc] matches any character that isn’t between the brackets.

---

# Vocabulary Table

|Word/Term|Simple English Definition|Arabic Translation|
|:--|:--|:--|
|**Regex**|A set of characters that defines a search pattern.|تعبير نمطي|
|**Quantifier**|A symbol that defines how many times a character should repeat.|محدد الكمية|
|**Greedy**|A behavior where the program tries to find the biggest match.|طماع / جشع|
|**Literal**|Matching a character exactly as it is, without special meaning.|حرفي|
|**Anchor**|Symbols used to fix a match to the start or end of a string.|مرساة|
|**Verbose**|Using more words than necessary to make something clear.|مطوّل / مفصل|
|**Substitution**|Replacing one piece of text with another.|استبدال|

---

# Key Takeaways

1. **Deduplication**: Regex replaces dozens of lines of manual checking with a single line of pattern code.
2. **Match vs. Search**: `search()` finds one match; `findall()` finds all of them.
3. **Safety First**: Use `re.VERBOSE` and comments for long, complex patterns to make them readable and easy to fix later.
4. **Anchors provide precision**: Using `^` and `$` ensures you aren't matching random fragments in the middle of data.
5. link https://pythex.org/ 