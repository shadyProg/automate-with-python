# Executive Summary

The primary goal of Chapter 3 is to introduce **functions**, which are essentially "miniprograms" within a larger program. The chapter addresses the problem of **duplicated code**—writing the same instructions multiple times—which makes programs long and difficult to maintain. By using functions, programmers can achieve **deduplication**, making their code shorter, easier to read, and more resilient to bugs.

---

# Deep-Dive Content: Functions

## 1. Defining and Calling Functions

Functions allow you to group code that performs a specific task so it can be reused throughout a program.

### 1.1 The `def` Statement

- A function is created using a **`def` statement**, which includes the function name and a block of code called the **body**.
- The code inside a function does not run when it is defined; it only runs when the function is **called**.

### 1.2 Function Calls

- A **function call** is the function’s name followed by parentheses `()`.
- When a program reaches a call, it "jumps" to the first line of the function and runs the code inside.
- Once the function ends, the program "jumps back" to the line that called it and continues.

## 2. Passing Information to Functions

You can send data to functions to change how they behave or what they calculate.

### 2.1 Parameters and Arguments

- **Parameters:** Variables listed in the function's definition that act as **placeholders** for data.
- **Arguments:** The actual values passed into the function during a call.
- **Data Flow:** When a function is called with arguments, those values are assigned to the parameters.

### 2.2 Return Values and `return` Statements

- A **return value** is the single value that a function "gives back" to the caller after finishing.
- The **`return` statement** specifies what value the function should send back.
- A function call evaluates to its return value, meaning it can be used inside expressions.

### 2.3 The `None` Value

- `None` represents the **absence of a value**.
- It is the only value in the **NoneType** data type.
- If a function does not have a `return` statement, it automatically returns `None` behind the scenes.
`
```
``` ->>> spam = print('Hello!') 
     ->>> Hello!
->>> None == spam
    ->>>  True
```

## 3. Organizing Code Execution

Python uses specific internal tools to manage how functions run and how variables are stored.

##### Keyword Arguments and the print() Function
بعض الكلمات بتضيفها علشان تعدل في print انت عايز تبطعه على شاشة 
```
print('Hello', end='') 
print('World')
 >>>  HelloWorld
 print('cats', 'dogs', 'mice')  
>>> cats dogs mice
 print('cats', 'dogs', 'mice', sep=',') 
>>> cats,dogs,mice

```
### 3.1 The Call Stack

- The **call stack** is how Python remembers where to return the execution after a function finishes.
- When a function is called, Python creates a **frame object** on top of the stack.
- When a function returns, Python "pops" the frame off the top to return to the original line.
كاتب شبها بقصة بتكلم مع شخص وجيت افتركت حاجة تعلمها تكلمك صبحك تاني ف تروح تكلمه وبعد كدا ترجع لصحبك الاول 
-- بمعنا لو شاف استدعاء لفانكش تانية هيروحلها هي 

![[Screenshot (80).png]]
```
a() starts
b() start
c() starts
c() returns
b() returns
d() starts
d() returns
a() returns
```

![[Screenshot (81).png]]
بس لاحظ انه بيعمل بيونتر على اول واحدة علشان مينساش هو كان فين وبعد كدا يعمل objects  حسب استدعاء ولما يخلص ي pop
- When the call stack is empty, the execution is on a line outside of all functions

### 3.2 Local and Global Scopes

- **Scope** is a "container" for variables. Variables exist in either a **local scope** (inside a function) or the **global scope** (outside all functions).
- **Local Variables:** These are created when a function is called and are **forgotten** (destroyed) when the function returns.
- **Global Variables:** These are created when the program starts and are forgotten when the program ends.

### 3.3 The 4 Rules of Scope

1. Variables outside all functions are always **global**.
2. If a function uses the **`global` statement** for a variable, that variable is global.
3. If a variable is used in an **assignment statement** inside a function, it is **local**.
4. If a variable is used in a function but not assigned a value there, it is **global**.
5. You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable also named spam
```
 def spam():
  print(eggs) 
eggs = 42 
spam() 
print(eggs)
 >>> eggs 
 >>> 42

```

#### The global Statement
```
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
>>> spam
```
---

```
def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is the global
    
eggs = 42 # this is the global
spam()
print(eggs)
>>> spam
```

مينفعش تستخدم ال global في local 
- حلي بالك الدوال بتبحث بشكل local علشان كدا ده هيبقى ايرور 
```
def spam():
    print(eggs)  # ERROR!
    eggs = 'spam local'

global eggs 
eggs = 'global'
spam()

```
- بس ينفع العكس  شبه المثال فوق spam  اول مثال 
##### ---  FUNCTIONS AS “BL ACK BOXES
مش لازم تعرف جوا بتشتغل ازاي مهم تعرف داخل وخارج ايه 
## 4. Error and Exception Handling

Programmers use specific tools to keep programs from crashing when an error occurs.

### 4.1 `try` and `except` Statements

- **Exceptions:** These are errors (like `ZeroDivisionError`) that cause a program to crash if not handled.
- **The Workflow:** Code that might fail is placed in a **`try` clause**. If an error happens, execution immediately moves to the **`except` clause**.
- **Benefit:** This makes programs more **resilient** to common mistakes or user errors.

---

# Vocabulary Table

| Word/Term        | Simple English Definition                                   | Arabic Translation |
| :--------------- | :---------------------------------------------------------- | :----------------- |
| **Deduplicate**  | To remove repeated or copied code.                          | إزالة التكرار      |
| **Placeholder**  | A name used to hold a spot for a real value later.          | عنصر نائب          |
| **Meandering**   | Moving in a slow, winding way.                              | متعرج / متجول      |
| **Encapsulate**  | To put something in a closed container to keep it separate. | تغليف / احتواء     |
| **Resilient**    | Strong and able to handle problems without breaking.        | مرن / قوي          |
| **Implicit**     | Something that happens automatically without being seen.    | ضمني               |
| **Frame Object** | A technical detail used by Python to store a function call. | كائن الإطار        |

---

# Key Takeaways

- Functions help you organize your code into small, manageable "miniprograms".
- Always try to **deduplicate** your code to make it easier to fix bugs later.
- **Local variables** are separate from each other; a bug in one function's variable won't affect other functions.
- Use **`try` and `except`** to handle errors gracefully instead of letting the program crash.
- Think of functions as **"black boxes"**: you only need to know what goes in (arguments) and what comes out (return values).