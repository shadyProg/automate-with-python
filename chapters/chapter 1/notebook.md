# Lecture Summary: Python Programming Foundations (Chapter 1)

## 1. The Python Execution Environment

- **The Python Interpreter**: The software layer that reads source code and executes instructions.
- **Interactive Shell (REPL)**: Standing for **Read-Evaluate-Print Loop**, this environment executes Python instructions one at a time and provides immediate feedback.
- **Source Code**: The set of instructions written in the Python language before being parsed by the interpreter.

## 2. Expressions and Operators

### 2.1 Definition of an Expression

An **expression** is the most fundamental instruction in Python, consisting of **values** and **operators**. Every expression must **evaluate** (reduce) down to a **single value**.

### 2.2 Mathematical Operators and Precedence

Python follows specific rules of **precedence** (order of operations) similar to standard mathematics.

|Operator|Operation|Precedence|Example|
|:--|:--|:--|:--|
|`**`|**Exponent**|Highest|`2 ** 3` evaluates to `8`|
|`%`|**Modulus** (Remainder)|Medium|`22 % 8` evaluates to `6`|
|`//`|**Integer Division** (Floored Quotient)|Medium|`22 // 8` evaluates to `2`|
|`/`|**Division**|Medium|`22 / 8` evaluates to `2.75`|
|`*`|**Multiplication**|Medium|`3 * 5` evaluates to `15`|
|`-`|**Subtraction**|Lowest|`5 - 2` evaluates to `3`|
|`+`|**Addition**|Lowest|`2 + 2` evaluates to `4`|

_Note: Parentheses `()` can be used to override standard precedence._

## 3. Data Types

A **data type** is a category for values; every value belongs to exactly one type.

- **Integers (int)**: Whole numbers (e.g., -2, 0, 42).
- **Floating-point numbers (float)**: Numbers containing a decimal point (e.g., 3.14, 42.0).
- **Strings (str)**: Textual data surrounded by single quotes (e.g., 'Hello').

### 3.1 String-Specific Operations

- **String Concatenation**: Using the `+` operator to join two string values into a new string.
- **String Replication**: Using the `*` operator between one string and one integer to repeat the string multiple times. _Replication cannot be performed between two strings or a string and a float_.

## 4. Variables and Memory Management

### 4.1 Assignment Statements

A **variable** is a labeled location in the computer's memory used to store a single value. Values are stored via **assignment statements**, consisting of a variable name, the **assignment operator** (`=`), and the value.

### 4.2 Overwriting and Initialization

- **Initialization**: Occurs the first time a value is stored in a variable.
- **Overwriting**: When a new value is assigned to an existing variable, the old value is forgotten.

### 4.3 Naming Constraints

Legal variable names must adhere to three strict rules:

1. Must be a **single word** (no spaces).
2. Must use only **letters, numbers, and underscores**.
3. **Cannot begin with a digit**. _Variable names are case-sensitive (e.g., `spam` and `SPAM` are distinct variables)_.

## 5. Core Built-in Functions

Functions are specialized instructions that can accept **arguments** (input) and return a **return value** (output).

- **`print()`**: Displays the string value passed to it on the screen.
- **`input()`**: Pauses execution to wait for user keyboard input; it **always returns a string value**, even if the user enters a number.
- **`len()`**: Accepts a string and evaluates to an **integer** representing the number of characters in that string.
- **Type Conversion Functions**:
    - **`str()`**: Converts a value to its string form.
    - **`int()`**: Converts a value to an integer (rounds floats down).
    - **`float()`**: Converts a value to a floating-point number.

## 6. Comparisons and Equivalence Logic

- **Integer vs. Float**: An integer is considered equal to its floating-point equivalent (e.g., `42 == 42.0` is `True`).
- **Numeric vs. String**: A number is **not equal** to its string version (e.g., `42 == '42'` is `False`) because they belong to different data types.

---

### ⚠️ Exam Traps & Important Notes

- **The Input Trap**: Remember that `input()` always returns a **string**. If you need to perform math on user input, you must explicitly wrap it in `int()` or `float()`.
- **Concatenation Errors**: Python does not allow the concatenation of a string and an integer using `+`. You must convert the integer to a string using `str()` first (e.g., `'Age: ' + str(29)`).
- **Division Distinction**: Be prepared to distinguish between `/` (true division, returns float), `//` (integer division, returns int), and `%` (modulus, returns remainder).
- **Syntactic Validity**: Variable names starting with a number (e.g., `42bacon`) or containing special characters (e.g., `total$`) will trigger a `SyntaxError`.
- **Case Sensitivity**: Exam questions involving variable lookups often use slight capitalization changes to trick students. `myVariable` is not the same as `myvariable`.
- **Rounding Behavior**: Using `int()` on a float does not follow standard rounding rules; it **truncates** (rounds down) to the nearest whole number (e.g., `int(7.7)` becomes `7`).