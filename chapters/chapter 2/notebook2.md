# Book Chapter Notes: Chapter 2 - Flow Control

## 1. Foundational Concepts of Flow Control

**Flow control statements** determine which Python instructions to execute under specific conditions, allowing programs to skip, repeat, or choose between multiple paths of execution. This moves beyond the sequential top-to-bottom execution established in **Chapter 1**.

### 1.1 Program Execution and Modeling

- **Program Execution**: Often referred to simply as **execution**, this is the term for the current instruction being processed by the interpreter.
- **Flowcharts**: A visual model of program logic.
    - **Diamonds**: Represent branching points or decisions.
    - **Rectangles**: Represent standard processing steps.
    - **Rounded Rectangles**: Represent the start and end points of the logic.

## 2. Boolean Logic and Relational Operators

### 2.1 The Boolean Data Type

The **Boolean** data type consists of exactly two values: **True** and **False**. In Python, these must be capitalized and are written without quotes.

### 2.2 Comparison (Relational) Operators

These operators compare two values and evaluate to a single Boolean value.

- **`==` (Equal to)**: Evaluates to True if values on both sides are identical.
- **`!=` (Not equal to)**: Evaluates to True if values are different.
- **Relational**: `<`, `>`, `<=`, `>=` (Less than, Greater than, and their "equal to" variations).

### 2.3 Boolean Operators

- **`and`**: A **binary operator**; evaluates to True only if **both** expressions are True.
- **`or`**: A **binary operator**; evaluates to True if **at least one** expression is True.
- **`not`**: A **unary operator**; evaluates to the **opposite** Boolean value of the expression.

## 3. Structural Elements of Flow Control

### 3.1 Conditions

A **condition** is an expression used in flow control statements that evaluates down to a Boolean value.

### 3.2 Blocks of Code

Lines of code grouped together via **indentation**.

- **Rules of Blocks**:
    - They begin when indentation increases.
    - They can contain other (nested) blocks.
    - They end when indentation decreases to zero or to the level of a containing block.

## 4. Control Flow Statements

### 4.1 Conditional Statements

- **`if` Statement**: Executes a block (clause) if the condition is True.
- **`else` Statement**: An optional fallback that executes only if all preceding conditions in the structure were False.
- **`elif` Statement**: Short for "else if." It provides a new condition if previous ones were False.
    - _Insight: In a chain of `if/elif` statements, Python executes only the first True clause and skips all subsequent `elif` clauses, regardless of their truth value_.

### 4.2 Iterative Statements (Loops)

- **`while` Loop**: Executes a clause repeatedly as long as the condition remains True.
    - **Iteration**: The term for each cycle through the loop's clause.
- **`for` Loop**: Used for a definite number of repetitions.
- **`range()` Function**: Generates a sequence of integers.
    - `range(stop)`: 0 up to (not including) the stop value.
    - `range(start, stop)`: Starts at the first integer, ends before the second.
    - `range(start, stop, step)`: Increments by the step value. _A negative step allows for counting down_.

### 4.3 Execution Modifiers

- **`break`**: Immediately exits the loop's clause.
- **`continue`**: Immediately jumps to the start of the loop to re-evaluate the condition.

## 5. Standard Library and Termination

- **Modules**: Related groups of functions that can be embedded in programs.
- **`import` Statements**: Used to make modules like `random` or `sys` available.
- **`sys.exit()`**: A function that terminates the program immediately, regardless of the current execution point.


## 6. Integration with Other Chapters

- This chapter utilizes the expressions and data types from **Chapter 1**.
- It provides the logical foundation for **Chapter 3**, which introduces **Functions** as a way to further organize code blocks into manageable chunks.

---

### Exam Traps & Chapter Pitfalls

- **Assignment vs. Comparison**: Confusion between the `=` (**assignment**) and `==` (**equal to**) operators is a frequent source of logic errors and `SyntaxError` crashes.
- **Boolean Capitalization**: Writing `true` or `false` instead of the required **`True`** or **`False`** will result in a `NameError`.
- **Implicit Truthiness**: In conditional contexts, `0`, `0.0`, and `''` (empty string) are considered **False** (**Falsey**). All other values are considered **True** (**Truthy**).
- **Elif Order**: Because Python stops checking a conditional chain after the first True result, the **order of `elif` statements is critical**. General conditions must follow specific ones to avoid unreachable code.
- **Range Boundaries**: The `range()` function is **exclusive** of the stop value; `range(5)` evaluates to 0, 1, 2, 3, 4.
- **Module Naming**: Never save a script with the same name as a standard module (e.g., `random.py`), as this will cause `import` statements to fail when they attempt to load your script instead of the library.