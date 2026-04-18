Below are the answers to the practice questions and details for the practice projects for Chapters 8 through 11, based on the provided sources.

---

### **Chapter 8: Input Validation**

#### **Practice Questions**

1. **Does PyInputPlus come with the Python Standard Library?** No, it is a third-party module and must be installed separately.
2. **Why is PyInputPlus commonly imported with `import pyinputplus as pyip`?** This is done to make the code shorter to type when calling functions.
3. **What is the difference between `inputInt()` and `inputFloat()`?** `inputInt()` returns an integer value, while `inputFloat()` returns a floating-point (decimal) value.
4. **How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?** By calling `pyip.inputInt(min=0, max=99)`.
5. **What is passed to the `allowRegexes` and `blockRegexes` keyword arguments?** A list of regular expression strings that the function should specifically allow or deny.
6. **What does `inputStr(limit=3)` do if blank input is entered three times?** It will raise a `RetryLimitException`.
7. **What does `inputStr(limit=3, default='hello')` do if blank input is entered three times?** The function will return the string `'hello'` instead of raising an exception.

#### **Practice Projects**

- **Sandwich Maker:** Write a program that asks the user for their sandwich preferences (bread, protein, cheese, etc.) using PyInputPlus functions like `inputMenu()` and `inputYesNo()`. The program should have a set of prices and display the total cost at the end.
- **Write Your Own Multiplication Quiz:** Create a timed multiplication quiz program without using the PyInputPlus module. It must handle 10 questions, give the user three tries per question, and mark them wrong if they take longer than 8 seconds to answer.

---

### **Chapter 9: Reading and Writing Files**

#### **Practice Questions**

1. **What is a relative path relative to?** It is relative to the current working directory.
2. **What does an absolute path start with?** It starts with the root folder, such as `C:\` on Windows or `/` on macOS/Linux.
3. **What does `Path('C:/Users') / 'Al'` evaluate to on Windows?** It evaluates to `WindowsPath('C:/Users/Al')`.
4. **What does `'C:/Users' / 'Al'` evaluate to on Windows?** It results in an error because the `/` operator cannot join two strings.
5. **What do `os.getcwd()` and `os.chdir()` do?** `os.getcwd()` returns the current working directory, and `os.chdir()` changes it.
6. **What are the `.` and `..` folders?** `.` is the current folder, and `..` is the parent folder.
7. **In `C:\bacon\eggs\spam.txt`, which part is the dir name and which is the base name?** `C:\bacon\eggs` is the directory name, and `spam.txt` is the base name.
8. **What are the three “mode” arguments for `open()`?** `'r'` for read, `'w'` for write, and `'a'` for append.
9. **What happens if an existing file is opened in write mode?** Its contents are completely erased and overwritten.
10. **What is the difference between `read()` and `readlines()`?** `read()` returns the entire file content as one string; `readlines()` returns a list of strings, one for each line.
11. **What data structure does a shelf value resemble?** It resembles a dictionary.

#### **Practice Projects**

- **Extending the Multi-Clipboard:** Update the `mcb.pyw` script to include a `delete <keyword>` command to remove a specific keyword and a `clear` command to delete all keywords from the shelf.
- **Mad Libs:** Create a program that reads a text file and replaces placeholders like `ADJECTIVE`, `NOUN`, and `VERB` by prompting the user for their own words, then saves the result to a new file.
- **Regex Search:** Write a script that opens every `.txt` file in a folder and searches for lines that match a user-provided regular expression, printing the results to the screen.

---

### **Chapter 10: Organizing Files**

#### **Practice Questions**

1. **What is the difference between `shutil.copy()` and `shutil.copytree()`?** `shutil.copy()` copies a single file; `shutil.copytree()` copies an entire folder and all its contents.
2. **What function is used to rename files?** `shutil.move()` is used for both moving and renaming.
3. **What is the difference between `send2trash` and `shutil` deletion functions?** `send2trash` moves items to the recycle bin (safe), while `shutil` functions delete them permanently.
4. **What `ZipFile` method is equivalent to `open()`?** The `zipfile.ZipFile()` function.

#### **Practice Projects**

- **Selective Copy:** Walk through a folder tree to find files with specific extensions (like `.pdf` or `.jpg`) and copy them into a new folder.
- **Deleting Unneeded Files:** Write a program that walks a folder tree and identifies exceptionally large files (e.g., over 100MB) and prints their absolute paths.
- **Filling in the Gaps:** Write a program that finds files with a specific prefix (like `spam001.txt`, `spam003.txt`) and renames them to close any gaps in the numbering.

---

### **Chapter 11: Debugging**

#### **Practice Questions**

1. **Assert statement for `spam < 10`:** `assert spam >= 10, 'The spam variable is less than 10.'`.
2. **Assert statement for `eggs` and `bacon` being the same (case-insensitive):** `assert eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same!'`.
3. **Assert statement that always triggers:** `assert False, 'This assertion always triggers.'`.
4. **Two lines needed for `logging.debug()`:** `import logging` and `logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')`.
5. **Two lines for logging to a file:** Same as above, but add `filename='programLog.txt'` to the `basicConfig()` call.
6. **The five logging levels:** DEBUG, INFO, WARNING, ERROR, and CRITICAL.
7. **How to disable all logging:** `logging.disable(logging.CRITICAL)`.
8. **Why is logging better than `print()`?** You can disable messages without removing code, categorize by level, and include timestamps.
9. **Step Over, Step In, and Step Out:** "Step In" enters a function call; "Step Over" runs the function quickly without entering it; "Step Out" finishes the current function and returns to the caller.
10. **When will the debugger stop after clicking Continue?** When it reaches the end of the program or a breakpoint.
11. **What is a breakpoint?** A setting on a line of code that causes the debugger to pause execution there.
12. **How to set a breakpoint in Mu:** Click the line number to make a red dot appear.

#### **Practice Project**

- **Debugging Coin Toss:** You are given a coin-toss guessing game script with several bugs. You must use debugging techniques to find and fix them (e.g., fixing variable misspellings like `guesss` and ensuring the program compares the same data types).