# Executive Summary

The primary goal of **Chapter 11: Debugging** is to equip students with specialized tools and techniques to identify, track, and fix the root causes of bugs in their programs. As programs grow in complexity, simple errors become harder to find by just reading the code. This chapter introduces three proactive methods—**Raising Exceptions**, **Assertions**, and **Logging**—which help detect bugs early. Finally, it teaches how to use the **Mu Debugger** to watch code execute one line at a time and inspect the real-time values of variables.

---

# Deep-Dive Content: Debugging

## 1. Raising Exceptions and Tracebacks

While Python automatically raises exceptions for invalid code, you can manually trigger them to handle anticipated errors or signal that a function has received invalid data.

### 1.1 The `raise` Statement

- **Purpose**: To stop the current function immediately and move the program execution to an `except` block.
- **Syntax**: Use the `raise` keyword followed by a call to `Exception()` with a helpful error message.
- **Example Code**:
    
    ```
    def boxPrint(symbol, width, height):
        if len(symbol) != 1:
            raise Exception('Symbol must be a single character string.') #
        # logic to print box...
    ```
    

### 1.2 Managing the Traceback

- **Definition**: A "treasure trove" of info containing the error message, the line number that caused it, and the sequence of function calls (the **call stack**) leading up to it.
- **Retrieving as a String**: Use the `traceback.format_exc()` function to get the error details as a string without crashing the program.
- **Logging Errors**: You can write these tracebacks to a text file to review later while keeping the program running.

## 2. Assertions

An assertion is a "sanity check" used to ensure that the code is not doing something obviously wrong from a logic standpoint.

### 2.1 The `assert` Statement

- **Logic**: "I assert that this condition is true; if not, there is a bug and the program should stop immediately".
- **Syntax**: `assert <condition>, <message_if_false>`.
- **Failing Fast**: Assertions help you find bugs sooner by crashing the program the moment a rule is broken, reducing the amount of code you need to check.

### 2.2 Assertions vs. Exceptions

- **Usage Rule**: Assertions are for **programmer errors** (things that should never happen); Exceptions are for **user or environmental errors** (things that might happen, like a missing file).
- **Disabling**: Users can turn off assertions for speed (using the `-O` flag), so they should never be used for critical user data validation.

## 3. Logging

Logging is a way to record custom messages that describe the internal flow of your program as it runs.

### 3.1 Why Logging is Better than `print()`

- **Categorization**: Messages can be grouped by importance using levels.
- **Easy Disabling**: You can turn off all log messages with one line of code (`logging.disable()`) rather than deleting dozens of `print()` calls manually.
- **File Storage**: You can direct log output to a text file using the `filename` argument in `basicConfig()` to keep your screen clear.

### 3.2 Logging Levels (Least to Most Important)

- **DEBUG**: Small details for diagnosing problems.
- **INFO**: General events or confirmation that things are working.
- **WARNING**: Potential future problems.
- **ERROR**: The program failed to do something.
- **CRITICAL**: Fatal error; the program must stop.

## 4. The Mu Debugger

The debugger is a tool that runs your program slowly—one line at a time—so you can inspect variable values in the **Debug Inspector** pane.

### 4.1 Control Buttons

- **Continue**: Run normally until the program ends or hits a "breakpoint."
- **Step In**: Move into the next line or inside a function call.
- **Step Over**: Run the next line; if it's a function, run it at full speed and pause when it returns.
- **Step Out**: Finish the current function at full speed and then pause at the caller.

### 4.2 Breakpoints

- **Definition**: A setting on a specific line of code that tells the debugger to pause there.
- **Usage**: In Mu, click the line number to create a red dot. This allows you to skip thousands of loop iterations and jump straight to the code you want to inspect.

---

# ⚠️ Important Author Warnings

- **Don't Debug with `print()`**: Removing `print()` calls after fixing a bug is tedious and error-prone; you might accidentally delete a message the user actually needs to see.
- **Assertions are Not for Users**: A user should never see an `AssertionError`. If an error is expected during normal use, use `try/except`.
- **Fail Fast**: It is better to have a program crash immediately when a bug occurs than to have it continue running with bad data, which can cause more damage.
- **Namespace Trap**: Never name your script `logging.py`, or Python will try to import your file instead of the actual logging module.

---

# 📘 Vocabulary Table

|Word/Term|Simple English Definition|Arabic Translation|
|:--|:--|:--|
|**Debugging**|The process of finding and fixing errors in code.|تصحيح الأخطاء|
|**Traceback**|A report showing the path and call stack of an error.|تتبع الخطأ|
|**Assertion**|A statement that a condition must be true for logic to hold.|تأكيد / جزم|
|**Sanity Check**|A quick test to see if something is obviously wrong.|فحص السلامة (المنطق)|
|**Logging**|Keeping a record of events as a program runs.|تسجيل الأحداث|
|**Breakpoint**|A point where the debugger pauses automatically.|نقطة توقف|
|**Call Stack**|The sequence of functions currently being executed.|مكدس الاستدعاءات|
|**Failing Fast**|Crashing immediately to avoid spreading bad data.|الفشل السريع|

---

# Key Takeaways

1. **Bugs are Normal**: Even professionals make bugs; the difference is the tools they use to find them.
2. **Logs > Prints**: Use the `logging` module to leave a "trail of breadcrumbs" that you can hide or show instantly.
3. **Use Assertions for Internal Logic**: Use `assert` to verify that your data structures are correct (e.g., ensuring a traffic light always has one red light).
4. **Debugger for Transparency**: When variable values seem wrong, use the debugger to watch them change step-by-step rather than guessing.
5. **Clean Handling**: Use `traceback.format_exc()` to record error details to a file while keeping the program user-friendly.