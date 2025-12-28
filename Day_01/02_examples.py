"""
Day 1: Python Basics - Code Examples
Run each section separately to see the output
"""

# ============================================
# SECTION 1: Variables and Data Types
# ============================================
print("=" * 50)
print("SECTION 1: Variables and Data Types")
print("=" * 50)

# Different data types
name = "Alice"          # String
age = 25               # Integer
height = 5.6           # Float
is_student = True      # Boolean

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Is Student: {is_student} (type: {type(is_student).__name__})")

# Type conversion examples
print("\nType Conversion:")
age_str = "30"
age_int = int(age_str)
print(f"'{age_str}' converted to integer: {age_int}")

price_int = 20
price_float = float(price_int)
print(f"{price_int} converted to float: {price_float}")

num = 100
num_str = str(num)
print(f"{num} converted to string: '{num_str}'")


# ============================================
# SECTION 2: Arithmetic Operators
# ============================================
print("\n" + "=" * 50)
print("SECTION 2: Arithmetic Operators")
print("=" * 50)

a = 17
b = 5

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponent: {a} ** 2 = {a ** 2}")

# Practical example: Calculate average
num1 = 85
num2 = 92
num3 = 78
average = (num1 + num2 + num3) / 3
print(f"\nGrades: {num1}, {num2}, {num3}")
print(f"Average: {average:.2f}")


# ============================================
# SECTION 3: Comparison Operators
# ============================================
print("\n" + "=" * 50)
print("SECTION 3: Comparison Operators")
print("=" * 50)

x = 10
y = 5

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= 10: {x >= 10}")
print(f"y <= 5: {y <= 5}")


# ============================================
# SECTION 4: Logical Operators
# ============================================
print("\n" + "=" * 50)
print("SECTION 4: Logical Operators")
print("=" * 50)

age = 22
has_id = True
is_member = False

print(f"Age: {age}, Has ID: {has_id}, Is Member: {is_member}")
print(f"Can enter (age >= 18 AND has_id): {(age >= 18) and has_id}")
print(f"Gets discount (age < 18 OR is_member): {(age < 18) or is_member}")
print(f"NOT is_member: {not is_member}")

# Combining logical operators
can_purchase = (age >= 21) and (has_id) and (not is_member)
print(f"Can purchase alcohol: {can_purchase}")


# ============================================
# SECTION 5: String Operations
# ============================================
print("\n" + "=" * 50)
print("SECTION 5: String Operations")
print("=" * 50)

first_name = "John"
last_name = "Doe"

# Concatenation
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Repetition
separator = "-" * 30
print(separator)

# String methods
text = "  Python Programming  "
print(f"Original: '{text}'")
print(f"Lowercase: '{text.lower()}'")
print(f"Uppercase: '{text.upper()}'")
print(f"Stripped: '{text.strip()}'")
print(f"Length: {len(text)}")


# ============================================
# SECTION 6: String Formatting
# ============================================
print("\n" + "=" * 50)
print("SECTION 6: String Formatting (f-strings)")
print("=" * 50)

name = "Alice"
age = 28
salary = 75000.50

# Basic f-string
print(f"Employee: {name}, Age: {age}")

# Expressions in f-strings
print(f"In 5 years, {name} will be {age + 5} years old")

# Formatting numbers
print(f"Salary: ${salary:,.2f}")  # Add comma separator and 2 decimals

# Alignment
print(f"{'Name':<10} {'Age':<5} {'Salary':<12}")
print(f"{name:<10} {age:<5} ${salary:<11,.2f}")


# ============================================
# SECTION 7: Input and Output
# ============================================
print("\n" + "=" * 50)
print("SECTION 7: Input and Output")
print("=" * 50)

# Note: Uncomment the lines below to test interactive input
# This section is commented out so the file can run without waiting for input

"""
# Getting user input
user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")

# Getting numeric input
user_age = int(input("Enter your age: "))
print(f"You are {user_age} years old")
years_to_30 = 30 - user_age
print(f"You have {years_to_30} years until you're 30")
"""

# Print statement variations
print("\nPrint variations:")
print("Multiple", "values", "separated", "by", "spaces")
print("Custom", "separator", sep=" | ")
print("No newline at end", end=" -> ")
print("Continues here")


# ============================================
# SECTION 8: Practical Examples
# ============================================
print("\n" + "=" * 50)
print("SECTION 8: Practical Examples")
print("=" * 50)

# Example 1: Temperature Conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Example 2: Shopping Cart
item_name = "Laptop"
price = 899.99
quantity = 2
tax_rate = 0.08

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"\n--- Receipt ---")
print(f"Item: {item_name}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
print(f"---------------")

# Example 3: Circle calculations
radius = 7
pi = 3.14159

area = pi * (radius ** 2)
circumference = 2 * pi * radius

print(f"\nCircle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

# Example 4: Data type checking
values = [42, 3.14, "Hello", True, None]
print("\nData type checking:")
for value in values:
    print(f"{value} is of type: {type(value).__name__}")


# ============================================
# SECTION 9: Common Mistakes to Avoid
# ============================================
print("\n" + "=" * 50)
print("SECTION 9: Common Mistakes to Avoid")
print("=" * 50)

# Mistake 1: Type mismatch
age_string = "25"
# This would cause an error: result = age_string + 5
# Correct way:
result = int(age_string) + 5
print(f"Correct: {result}")

# Mistake 2: Integer division in Python 2 vs 3
print(f"In Python 3, 5/2 = {5/2} (float)")
print(f"Use floor division for integer result: 5//2 = {5//2}")

# Mistake 3: Variable naming
# Wrong: my-variable, 2nd_place, class
# Correct:
my_variable = "correct"
second_place = "correct"
class_name = "correct"

print("\nAll examples completed successfully!")
print("=" * 50)
