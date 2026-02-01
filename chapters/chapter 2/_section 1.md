# Lecture Summary: Flow Control (Chapter 2)

## 1. Boolean Logic and Data Types

### 1.1 The Boolean Data Type

Unlike integers or strings which have infinite possible values, the **Boolean** data type contains exactly two values: **True** and **False**.

- **Case Sensitivity**: In Python, Boolean values must be capitalized. Using `true` or `false` results in a `NameError`.

### 1.2 Boolean Operators

Python utilizes three logical operators to evaluate Boolean expressions:

- **and**: A **binary operator** that evaluates to `True` only if **both** Boolean values are `True`.
- **or**: A **binary operator** that evaluates to `True` if **at least one** of the Boolean values is `True`.
- **not**: A **unary operator** that evaluates to the **opposite** Boolean value of its operand.

## 2. Comparison and Relational Operators

**Comparison operators** evaluate expressions down to a single Boolean value by comparing two operands.

|Operator|Meaning|Data Type Support|
|:--|:--|:--|
|`==`|**Equal to**|All types|
|`!=`|**Not equal to**|All types|
|`<`|**Less than**|Integers and Floats only|
|`>`|**Greater than**|Integers and Floats only|
|`<=`|**Less than or equal to**|Integers and Floats only|
|`>=`|**Greater than or equal to**|Integers and Floats only|

_Note: An integer is never equal to its string representation (e.g., `42 == '42'` is `False`)._
_>>> 42 == 42.0 True_ ; python combine scalar 

#### 2.1 THE DIFFERENCE BET WEEN THE == AND = OPER ATORS
• The == operator (equal to) asks whether two values are the same as each other. 
• The = operator (assignment) puts the value on the right into the variable on the left.
## 3. Structural Elements of Flow Control

### 3.1 Conditions and Blocks

- **Condition**: An expression that evaluates to a Boolean value, used to decide the path of execution.
- **Block (Clause)**: A grouping of lines of code defined by **indentation**.
    - A block begins when indentation increases.
    - A block ends when indentation decreases to zero or to a containing block's level.
    - طريقة في بايثون ان جمل fun , if , ...etc  بيتعلمها جوا ال blocks  وممكن بلوك جوا بلوك 

##### Mixing Boolean and Comparison Operators
![[Pasted image 20260125135006.png]]
### 3.2 Program Execution

Normal **execution** is sequential (top-to-bottom). Flow control statements allow the execution to skip or repeat specific clauses based on conditions.
"If you use your finger to trace through a program"

## 4. Conditional Statements

- **if Statement**: Executes its clause if the condition is `True`.
- **else Statement**: Provides a fallback clause that executes only if the preceding `if` condition is `False`.
- **elif Statement**: Short for "else if." It allows for multiple **mutually exclusive** conditions. Python checks `elif` statements in order until one evaluates to `True`, at which point the rest of the chain is skipped.
#### continue
while True:
    name = input("Enter your name: ")
    if name != "admin":
        continue

    password = input("Enter your password: ")
    if password == "1234":
        print("Access granted")
        break
## 5. Iterative Statements (Loops)

### 5.1 while Loops

The **while loop** repeats a block of code as long as its condition remains `True`. The condition is checked at the **start** of every **iteration**.

### 5.2 for Loops and the range() Function

The **for loop** is used for **definite iteration**, often used to execute a block a specific number of times.

- **range(stop)**: Starts at 0 and goes up to, but does not include, the stop value.
- **range(start, stop)**: Specifies a starting integer.
- **range(start, stop, step)**: Specifies the increment (step) between each number. _A negative step can be used to count down_.

## 6. Control Flow Modifiers

- **break**: Immediately exits the current loop, moving execution to the code following the loop.
- **continue**: Immediately jumps back to the start of the loop to re-evaluate the condition for the next iteration.

## 7. Modules and Environment Control

- **import Statements**: Used to include functions from the **Standard Library** (e.g., `import random` for `randint()`).
- **sys.exit()**: Terminates the program execution immediately regardless of its position in the code.

##### DON’T OVERWRITE MODULE NAMES
- such as random.py, sys.py, os.py, or math.py
##### can use
import random, sys, os, math

#### from import Statements
بيقولك لما تستدخدم هذه الصيغة تبقى اكثر وضوحا علشان بتحدد  الفانكشن البتستعملها بس متستخدمهاش مع * لنك كدا هتعمل import  كلها وممكن متكنش واضحة 

## أفضل ممارسة (Best Practice)

✅ استخدم:

`import random`

أو لو محتاج دوال محددة فقط:

`from random import randint, choice`

❌ وتجنب:

`from random import *`



## مشكلة `from random import *`

- لا تعرف بالضبط ما الذي تم استيراده
    
- ممكن يحصل **تداخل أسماء (Name Collision)**
    
- الكود يكون أقل وضوحًا
    

مثال مشكلة:

`from random import *  
	def randint():    
		print("My function")`

هنا حصل تضارب ومصدر المشكلة غير واضح بسهولة.


#### difference
from random import *

print(randint(1, 10))
_بدون random._

المقارنة مع الطريقة الأفضل

 - الطريقة الشائعة والمفضّلة:
import random

print(random.randint(1, 10))



---

### ⚠️ Exam Traps & Important Notes

- **Assignment vs. Comparison**: A single equals sign (`=`) is for **assignment**; a double equals sign (`==`) is for **comparison**. Confusing these is a frequent source of `SyntaxError` or logic bugs.
- **Elif Order**: The order of `elif` statements matters. Since Python stops at the first `True` condition, placing a broad condition before a specific one (e.g., `age > 10` before `age > 100`) will cause the second block to be unreachable.
- **Truthy and Falsey Values**: In condition contexts, `0`, `0.0`, and `''` (empty string) are considered **False**. All other values are generally considered **True**.
- **Infinite Loops**: A `while True:` loop will run forever unless it contains a `break` statement or the user sends a `KeyboardInterrupt` (Ctrl-C).
- **The range() Boundary**: Remember that `range(5)` generates 0, 1, 2, 3, 4. The **stop value is never included** in the result.
- **Import Naming**: Never name your script the same as a standard module (e.g., `random.py`), as this will cause the `import` statement to load your file instead of the library module.

---

# ==vocabulary== 
---
 
| الكلمة (English)  | المعنى بالعربي      | السياق في شابتر 2                                                   |
| :---------------- | :------------------ | :------------------------------------------------------------------ |
| **Clause**        | بند / فقرة          | مجموعة الأكواد التي تلي جملة التحكم (مثل block الكود بعد if).       |
| **Evaluate**      | يُقيّم / يحسب       | عملية اختصار التعبيرات البرمجية لتصل إلى قيمة واحدة.                |
| **Equivalent**    | مكافئ / مساوٍ       | لوصف شيئين لهما نفس القيمة أو النتيجة.                              |
| **Exclusive**     | حصري / مانع للغير   | تستخدم لوصف حالات (elif) حيث يتم تنفيذ خيار واحد فقط من عدة خيارات. |
| **Indentation**   | إزاحة / مسافة بادئة | المسافات في بداية السطر التي تحدد تبعية الكود لكتلة معينة.          |
| **Corresponding** | مقابل / مماثل       | لوصف الأجزاء التي تتماثل بين الكود والمخطط الانسيابي.               |
| **Mandatory**     | إلزامي              | شيء يجب القيام به أو إدخاله (مثل الحاجة لإدخال كلمة مرور).          |
| **Ambiguous**     | غامض                | يستخدم لوصف المواقف التي تحتمل أكثر من معنى في المنطق البرمجي.      |
| **alternative**   | بديل                |                                                                     |

