# Executive Summary

The primary goal of **Chapter 8: Input Validation** is to teach readers how to ensure that the data entered by a user is correct and in the right format before the program processes it. Without validation, programs can crash or develop logic errors (such as a bank program accepting a negative number for a withdrawal). While programmers can write manual loops to check data, the chapter introduces the **PyInputPlus** module as a professional, time-saving tool to handle these tasks automatically.

---

# Deep-Dive Content: Input Validation

## 1. The Basics of Input Validation

Input validation code checks that user-entered values (like text from `input()`) are formatted correctly.

### 1.1 Why Validation Matters

- **Preventing Crashes**: It ensures the program doesn't receive the wrong data type (e.g., text when it expects a number).
- **Security**: Validating input can prevent vulnerabilities or logic bugs.
- **Manual Method**: A common manual pattern involves a `while True` loop, a `try/except` block to catch errors, and `continue`/`break` statements to control the flow.
- **Example Code (Manual Validation)**:
    
    ```
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
    ```
    

## 2. The PyInputPlus Module

PyInputPlus is a third-party module that provides functions similar to `input()` but includes built-in validation features.

### 2.1 Installation and Setup

- **Not Standard**: PyInputPlus is not part of the Python Standard Library and must be installed via Pip: `pip install --user pyinputplus`.
- **Importing**: It is common to import it with the alias `pyip` to save typing: `import pyinputplus as pyip`.

### 2.2 Core Validation Functions

The module provides specialized functions for different data types:
>You can also pass a custom validation function to it

- `inputStr()` : Is like the built-in input() function but has the general PyInputPlus features. You can also pass a custom validation function to it

- **`inputNum()`**: Ensures the user enters a number (int or float).
- **`inputInt()` / `inputFloat()`**: Specifically ensures an integer or a floating-point number.
- **`inputYesNo()`**: Ensures a "yes" or "no" response.
- `inputBool()` Is similar to inputYesNo(), but takes a “True” or “False” response and returns a Boolean value
- **`inputChoice()`**: Forces the user to pick from a specific list of options.
- `inputMenu()` : Is similar to inputChoice(), but provides a menu with numbered or lettered options.
- `inputDatetime()` :  Ensures the user enters a date and time
- **`inputEmail()`**: Ensures a valid email address is entered.
- **`inputPassword()`**: Displays `*` characters while the user types for privacy.
- `inputFilepath()` Ensures the user enters a valid file path and filename, and can optionally check that a file with that name exists

## 3. Customizing Validation with Keyword Arguments

PyInputPlus functions include optional arguments that make validation much more powerful without extra code.
### 3.0 Prompt
```
import pyinputplus as pyip

userInput=pyip.inputInt(prompt='Enter your age: ', min=5)

print(f'Your age is {userInput}.')

```
### 3.1 Range and Type Constraints

- **`min`, `max`, `greaterThan`, `lessThan`**: These arguments specify a range of valid numbers.
- **`blank=True`**: By default, blank input is not allowed. Setting this to `True` makes the input optional.

```
>>> import pyinputplus as pyip
>>> response = pyip.inputNum('Enter num: ', min=4)
Enter num:3
Input must be at minimum 4.
Enter num:4
>>> response
4
>>> response = pyip.inputNum('Enter num: ', greaterThan=4)
Enter num: 4
Input must be greater than 4.
Enter num: 5
>>> response
5
>>> response = pyip.inputNum('>', min=4, lessThan=6)
Enter num: 6
Input must be less than 6.
Enter num: 3
Input must be at minimum 4.
Enter num: 4
>>> response
4
```
_The blank Keyword Argument_
- By default, blank input isn’t allowed unless the blank keyword argument is set to True:

```
>>> import pyinputplus as pyip
>>> response = pyip.inputNum('Enter num: ')
Enter num:(blank input entered here)
Blank values are not allowed.
Enter num: 42
>>> response
42
>>> response = pyip.inputNum(blank=True)
(blank input entered here)
>>> response
''
```
### 3.2 Retries and Timeouts
 - pass argument to Timeout or end ask user because this module in default ask user for ever
 
- **`limit`**: Determines how many times the program asks for input before giving up and _raising_  a `RetryLimitException`. *that mean exception*
- **`timeout`**: Sets a time limit (in seconds) for the user to respond before raising a `TimeoutException`.
	 يعني هدخل input في حدود مدة الهكتبها ولو معملتش كدا هيرمي exception

- **`default`**: If a `limit` or `timeout` is reached, the function will return the `default` value instead of crashing with an exception.
	 بدل ما يرمي exception  ممكن نحط داتا ك N\A  default


### 3.3 Regular Expression Validation

- **`allowRegexes`**: A list of regex strings that the function will always *accept.

> مفيدة لو هتدخل ارقام رومانية 

```
>>> import pyinputplus as pyip
>>> response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
XLII
>>> response
'XLII'
>>> response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
xlii
>>> response
'xlii
```

- **`blockRegexes`**: A list of regex strings that the function will always *reject.
- **Note**: The "allow" list overrides the "block" list if a string matches both.
```
>>> import pyinputplus as pyip
>>> response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'],
blockRegexes=[r'cat'])
cat
This response is invalid.
catastrophe
This response is invalid.
category
>>> response
'category'
```
> حلي بالك لو ضفت ايه حاجة تاية مثل abc  هيقبله عادي 


## 4. Custom Validation Logic

If the built-in functions don't fit your needs, you can create your own logic.

### 4.1 The `inputCustom()` Function

- You write a function that accepts a string, performs checks, and raises an exception if the check fails.
> be carefull how pass function inside function 
- **Example Code**:
    
    ```
    import pyinputplus as pyip
    def addsUpToTen(numbers):
        numbersList = list(numbers)
        for i, digit in enumerate(numbersList):
            numbersList[i] = int(digit)
        if sum(numbersList) != 10:
            raise Exception('The digits must add up to 10.')
        return int(numbers)
    
    response = pyip.inputCustom(addsUpToTen) # No parentheses here
    ```
    

---

# ⚠️ Important Warnings & Notes

- **External Installation**: Because PyInputPlus is a third-party module, your program will not run on another computer unless that computer also has the module installed.
- **Passing Functions**: When using `inputCustom(addsUpToTen)`, do **not** add parentheses to the function name. You are passing the function itself, not calling it.
- **Exceptions**: Always wrap `limit` and `timeout` logic in a `try/except` block unless you provide a `default` value, or your program will crash when the limit is reached.
- **Passwords**: Even though `inputPassword()` hides characters on the screen, you should never store the actual password strings in your source code.

---

# 📘 Vocabulary Table

|Word/Term|Simple English Definition|Arabic Translation|
|:--|:--|:--|
|**Validation**|Checking if data is correct and follows rules.|التحقق من الصحة|
|**Tedious**|Boring, repetitive, and taking too much time.|ممل / مرهق|
|**Alias**|A shorter name used to refer to a module (like `pyip`).|اسم مستعار|
|**Prompt**|A message that asks the user for information.|رسالة حث / تنبيه|
|**Fallback**|A default value used when something goes wrong.|قيمة احتياطية|
|**Exception**|A signal that an error happened during a program.|استثناء (خطأ برمجي)|
|**Mandatory**|Something that must be done; not optional.|إلزامي|

---

# Key Takeaways

1. Input validation is critical for making programs "robust" (strong) against user mistakes.
2. **PyInputPlus** replaces the need for complex `while` loops and `try/except` blocks.
3. Functions like `inputInt()` return the correct data type (an integer) instead of a string, saving you a conversion step.
4. Use **`limit`** and **`timeout`** to prevent a program from waiting forever for a user response.
5. **`inputCustom()`** allows you to apply any specific logic to user input that the module doesn't already provide.

### Exam Traps & Chapter Pitfalls

- **Standard Library Confusion**: Students often think `pyinputplus` is built-in. It is **third-party** and must be installed.
- **Return Types**: Remember that `input()` always returns a string, but `pyip.inputInt()` returns an **integer**.
- **Exception Names**: The specific exceptions raised are `RetryLimitException` and `TimeoutException`.
- **The Default Rule**: If you use a `default` keyword argument, the `limit` and `timeout` exceptions are **not** raised; the program just uses the default value.