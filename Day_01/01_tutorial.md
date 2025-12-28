# Day 1: Python Basics & Setup
## Welcome to Your Python Journey! 🐍

---

## 📋 Today's Goals
By the end of Day 1, you will:
- ✅ Set up Python development environment
- ✅ Understand variables and data types
- ✅ Work with basic operators
- ✅ Handle input/output operations
- ✅ Write clean, well-commented code

---

## 🛠️ Part 1: Setting Up Your Environment

### Step 1: Install Python
1. Download Python from [python.org](https://www.python.org/downloads/)
2. **Important**: Check "Add Python to PATH" during installation
3. Verify installation:
```bash
python --version
# Should show: Python 3.x.x
```

### Step 2: Install a Code Editor
**Recommended**: Visual Studio Code
- Download from [code.visualstudio.com](https://code.visualstudio.com/)
- Install Python extension (by Microsoft)

**Alternative**: PyCharm Community Edition

### Step 3: Understanding pip
`pip` is Python's package manager (pre-installed with Python 3.4+)
```bash
pip --version
pip install <package_name>
pip list  # Show installed packages
```

### Step 4: Virtual Environments (Important for Data Science!)
Virtual environments keep project dependencies isolated.

```bash
# Create a virtual environment
python -m venv myenv

# Activate it
# Windows:
myenv\Scripts\activate
# Mac/Linux:
source myenv/bin/activate

# Deactivate
deactivate
```

---

## 📝 Part 2: Python Basics

### 2.1 Your First Python Program

Create a file `hello.py`:
```python
# This is a comment - Python ignores this line
print("Hello, World!")  # This prints text to the screen
```

**Run it**:
```bash
python hello.py
```

### 2.2 Comments
```python
# Single-line comment

"""
Multi-line comment
or docstring
Useful for documentation
"""

'''
Another way to write
multi-line comments
'''
```

**Best Practice**: Use comments to explain *why*, not *what*

---

## 🔢 Part 3: Variables and Data Types

### What is a Variable?
A variable is a container that stores data.

```python
# Variable assignment
name = "Alice"
age = 25
height = 5.6
is_student = True

# Python is dynamically typed - you don't declare types
x = 10       # x is an integer
x = "Hello"  # Now x is a string (perfectly valid!)
```

### Variable Naming Rules
✅ **Valid**:
- `user_name`, `userName`, `user2`, `_private`

❌ **Invalid**:
- `2user` (can't start with number)
- `user-name` (no hyphens)
- `class` (reserved keyword)

**Convention**: Use `snake_case` for variables (Python style guide - PEP 8)

---

## 📊 Part 4: Data Types

### 4.1 Integers (`int`)
Whole numbers, positive or negative
```python
age = 25
temperature = -5
big_number = 1_000_000  # Underscores for readability

print(type(age))  # <class 'int'>
```

### 4.2 Floats (`float`)
Decimal numbers
```python
price = 19.99
pi = 3.14159
scientific = 2.5e-3  # 0.0025

print(type(price))  # <class 'float'>
```

### 4.3 Strings (`str`)
Text data, enclosed in quotes
```python
name = "Alice"
message = 'Hello, World!'
multiline = """This is a
multi-line
string"""

# String concatenation
full_name = "Alice" + " " + "Smith"

# String repetition
stars = "*" * 10  # "**********"

print(type(name))  # <class 'str'>
```

### 4.4 Booleans (`bool`)
True or False values
```python
is_valid = True
is_empty = False

print(type(is_valid))  # <class 'bool'>
```

### Type Conversion
```python
# String to integer
age_str = "25"
age_int = int(age_str)  # 25

# Integer to string
num = 100
num_str = str(num)  # "100"

# String to float
price_str = "19.99"
price_float = float(price_str)  # 19.99

# Integer to float
x = 5
y = float(x)  # 5.0
```

---

## ➕ Part 5: Operators

### 5.1 Arithmetic Operators
```python
a = 10
b = 3

addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.333... (always returns float)
floor_division = a // b # 3 (integer division)
modulus = a % b         # 1 (remainder)
exponent = a ** b       # 1000 (10^3)

# Shorthand operators
x = 5
x += 2  # x = x + 2 → 7
x -= 1  # x = x - 1 → 6
x *= 3  # x = x * 3 → 18
x /= 2  # x = x / 2 → 9.0
```

### 5.2 Comparison Operators
Return `True` or `False`
```python
a = 10
b = 5

equal = (a == b)           # False
not_equal = (a != b)       # True
greater = (a > b)          # True
less = (a < b)             # False
greater_equal = (a >= 10)  # True
less_equal = (a <= 5)      # False
```

### 5.3 Logical Operators
```python
# AND - both conditions must be True
age = 25
has_license = True
can_drive = (age >= 18) and has_license  # True

# OR - at least one condition must be True
is_weekend = False
is_holiday = True
can_relax = is_weekend or is_holiday  # True

# NOT - inverts the boolean
is_raining = False
is_sunny = not is_raining  # True
```

---

## 💬 Part 6: Input and Output

### Output with `print()`
```python
# Basic printing
print("Hello, World!")

# Multiple values
name = "Alice"
age = 25
print("Name:", name, "Age:", age)

# Custom separator
print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry

# Custom end (default is newline)
print("Loading", end="...")
print("Done!")
# Output: Loading...Done!
```

### String Formatting (Modern Way)
```python
# f-strings (Python 3.6+) - RECOMMENDED
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Expressions inside f-strings
price = 19.99
quantity = 3
print(f"Total: ${price * quantity}")

# Formatting numbers
pi = 3.14159
print(f"Pi rounded: {pi:.2f}")  # 3.14
```

### Input from User
```python
# Get user input (always returns a string)
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Converting input to numbers
age_str = input("Enter your age: ")
age = int(age_str)  # Convert to integer
print(f"Next year you'll be {age + 1}")

# Shorthand
age = int(input("Enter your age: "))
```

---

## 🎨 Part 7: Code Formatting Best Practices (PEP 8)

### Indentation
- Use **4 spaces** per indentation level
- Never mix tabs and spaces

### Line Length
- Keep lines under 79 characters

### Blank Lines
- 2 blank lines between functions
- 1 blank line between logical sections

### Naming Conventions
```python
# Variables and functions: snake_case
user_name = "Alice"
total_price = 100

# Constants: UPPER_CASE
MAX_SIZE = 100
PI = 3.14159

# Classes: PascalCase (you'll learn later)
class UserProfile:
    pass
```

---

## 🧪 Part 8: Practice Exercises

### Exercise 1: Personal Info
Write a program that:
1. Asks for user's name, age, and city
2. Prints a formatted message

**Expected Output**:
```
Enter your name: Alice
Enter your age: 25
Enter your city: New York
Hello Alice! You are 25 years old and live in New York.
```

### Exercise 2: Simple Calculator
Create a calculator that:
1. Takes two numbers from user
2. Performs addition, subtraction, multiplication, division
3. Displays all results

### Exercise 3: Temperature Converter
Convert Celsius to Fahrenheit
- Formula: F = (C × 9/5) + 32
- Get temperature in Celsius from user
- Display in Fahrenheit

### Exercise 4: Area Calculator
Calculate area of a rectangle:
1. Get length and width from user
2. Calculate area (length × width)
3. Calculate perimeter (2 × (length + width))
4. Display results

### Exercise 5: Shopping Total
Calculate shopping bill:
1. Input item name, price, and quantity
2. Calculate subtotal (price × quantity)
3. Calculate tax (subtotal × 0.08)
4. Calculate total (subtotal + tax)
5. Display formatted receipt

---

## 🎯 Mini-Project: Advanced Calculator

Create `calculator.py` with the following features:
- Display a menu of operations (+, -, *, /, **, %, //)
- Get two numbers from user
- Perform selected operation
- Display result with proper formatting
- Handle division by zero

**Bonus**:
- Add modulus (%) and exponent (**) operations
- Format output to 2 decimal places

---

## 📚 Additional Resources

### Documentation
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 Style Guide](https://pep8.org/)

### Practice Platforms
- [HackerRank - Python](https://www.hackerrank.com/domains/python)
- [Codewars](https://www.codewars.com/)
- [LeetCode - Easy Problems](https://leetcode.com/)

### Videos
- freeCodeCamp Python Tutorial for Beginners
- Corey Schafer - Python Basics

---

## ✅ Day 1 Checklist

Before moving to Day 2, ensure you can:
- [ ] Install and run Python successfully
- [ ] Create and run `.py` files
- [ ] Declare variables with different data types
- [ ] Use arithmetic, comparison, and logical operators
- [ ] Take user input and display output
- [ ] Write clean code with comments
- [ ] Complete all 5 exercises
- [ ] Build the calculator mini-project

---

## 🚀 What's Next?

**Tomorrow (Day 2)**: Control Flow & Functions
- Conditional statements (if/else)
- Loops (for/while)
- Functions and lambda expressions

**Homework**:
1. Complete all exercises in `exercises.py`
2. Build the calculator project
3. Read about control flow in Python docs

---

**Remember**: Don't rush! Understanding fundamentals is crucial for data science and AI engineering. Practice each concept before moving forward.

Happy Coding! 🎉
