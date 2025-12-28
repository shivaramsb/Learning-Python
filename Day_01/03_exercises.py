"""
Day 1: Practice Exercises
Complete each exercise below. Solutions are at the bottom of the file.
Try to solve them yourself before looking at the solutions!
"""

# ============================================
# EXERCISE 1: Personal Information
# ============================================
"""
Write a program that:
1. Asks for the user's name, age, and city
2. Calculates the year they were born (current year is 2025)
3. Prints a formatted message with all this information

Expected output:
Enter your name: Alice
Enter your age: 25
Enter your city: New York
Hello Alice! You are 25 years old and live in New York.
You were born in approximately 2000.
"""

print("EXERCISE 1: Personal Information")
print("-" * 50)

# YOUR CODE HERE





# ============================================
# EXERCISE 2: Simple Math Operations
# ============================================
"""
Write a program that:
1. Takes two numbers from the user
2. Performs and displays: addition, subtraction, multiplication, division
3. Also shows floor division, modulus, and exponentiation

Expected output:
Enter first number: 17
Enter second number: 5
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3.4
17 // 5 = 3
17 % 5 = 2
17 ** 5 = 1419857
"""

print("\n\nEXERCISE 2: Simple Math Operations")
print("-" * 50)

# YOUR CODE HERE





# ============================================
# EXERCISE 3: Temperature Converter
# ============================================
"""
Write a temperature converter that:
1. Takes temperature in Celsius from user
2. Converts it to Fahrenheit using: F = (C * 9/5) + 32
3. Converts it to Kelvin using: K = C + 273.15
4. Displays all three temperatures with 2 decimal places

Expected output:
Enter temperature in Celsius: 25
25.00°C = 77.00°F = 298.15K
"""

print("\n\nEXERCISE 3: Temperature Converter")
print("-" * 50)

# YOUR CODE HERE





# ============================================
# EXERCISE 4: Rectangle Calculator
# ============================================
"""
Write a program that:
1. Takes length and width of a rectangle from user
2. Calculates and displays:
   - Area (length × width)
   - Perimeter (2 × (length + width))
   - Diagonal (use formula: √(length² + width²))
     For square root, use: ** 0.5

Expected output:
Enter length: 10
Enter width: 5
Area: 50.00
Perimeter: 30.00
Diagonal: 11.18
"""

print("\n\nEXERCISE 4: Rectangle Calculator")
print("-" * 50)

# YOUR CODE HERE





# ============================================
# EXERCISE 5: Shopping Receipt
# ============================================
"""
Write a program that:
1. Takes item name, price, and quantity from user
2. Calculates:
   - Subtotal (price × quantity)
   - Discount (10% if subtotal > 100, else 5%)
   - Tax (8% of subtotal after discount)
   - Total (subtotal - discount + tax)
3. Displays a formatted receipt

Expected output:
Enter item name: Laptop
Enter price: 899.99
Enter quantity: 2

----- RECEIPT -----
Item: Laptop
Price: $899.99
Quantity: 2
Subtotal: $1799.98
Discount: $179.98 (10%)
Tax: $129.60 (8%)
Total: $1749.60
-------------------
"""

print("\n\nEXERCISE 5: Shopping Receipt")
print("-" * 50)

# YOUR CODE HERE





# ============================================
# EXERCISE 6: BMI Calculator
# ============================================
"""
Write a BMI (Body Mass Index) calculator that:
1. Takes weight in kilograms and height in meters
2. Calculates BMI using: BMI = weight / (height ** 2)
3. Displays the BMI with 1 decimal place
4. Shows a category:
   - Underweight: BMI < 18.5
   - Normal: 18.5 <= BMI < 25
   - Overweight: 25 <= BMI < 30
   - Obese: BMI >= 30

Expected output:
Enter weight (kg): 70
Enter height (m): 1.75
Your BMI: 22.9
Category: Normal weight
"""

print("\n\nEXERCISE 6: BMI Calculator")
print("-" * 50)

# YOUR CODE HERE





# ============================================
# EXERCISE 7: Time Converter
# ============================================
"""
Write a program that:
1. Takes a number of seconds from user
2. Converts it to hours, minutes, and seconds
3. Displays in format: HH:MM:SS

Hints:
- hours = total_seconds // 3600
- minutes = (remaining_seconds) // 60
- seconds = remaining_seconds % 60

Expected output:
Enter seconds: 3665
3665 seconds = 1:01:05
"""

print("\n\nEXERCISE 7: Time Converter")
print("-" * 50)

# YOUR CODE HERE





# ============================================
# EXERCISE 8: Compound Interest Calculator
# ============================================
"""
Write a compound interest calculator that:
1. Takes principal amount, annual interest rate (%), and years
2. Calculates final amount using: A = P(1 + r/100)^t
3. Calculates total interest earned
4. Displays both amounts

Expected output:
Principal amount: 10000
Annual interest rate (%): 5
Number of years: 3
Final amount: $11576.25
Interest earned: $1576.25
"""

print("\n\nEXERCISE 8: Compound Interest Calculator")
print("-" * 50)

# YOUR CODE HERE





print("\n" + "=" * 50)
print("Exercises completed! Check solutions below.")
print("=" * 50)


# ============================================
# SOLUTIONS
# ============================================
"""
Don't look below until you've tried the exercises yourself!


.
.
.
.
.
.
.
.
.
.
SOLUTIONS BELOW
.
.
.
.
.
.
.
.
.
.
"""

# SOLUTION 1: Personal Information
def solution_1():
    print("\n\nSOLUTION 1: Personal Information")
    print("-" * 50)
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    
    current_year = 2025
    birth_year = current_year - age
    
    print(f"Hello {name}! You are {age} years old and live in {city}.")
    print(f"You were born in approximately {birth_year}.")


# SOLUTION 2: Simple Math Operations
def solution_2():
    print("\n\nSOLUTION 2: Simple Math Operations")
    print("-" * 50)
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {num1 / num2}")
    print(f"{num1} // {num2} = {num1 // num2}")
    print(f"{num1} % {num2} = {num1 % num2}")
    print(f"{num1} ** {num2} = {num1 ** num2}")


# SOLUTION 3: Temperature Converter
def solution_3():
    print("\n\nSOLUTION 3: Temperature Converter")
    print("-" * 50)
    celsius = float(input("Enter temperature in Celsius: "))
    
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    
    print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")


# SOLUTION 4: Rectangle Calculator
def solution_4():
    print("\n\nSOLUTION 4: Rectangle Calculator")
    print("-" * 50)
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    
    area = length * width
    perimeter = 2 * (length + width)
    diagonal = (length**2 + width**2) ** 0.5
    
    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")
    print(f"Diagonal: {diagonal:.2f}")


# SOLUTION 5: Shopping Receipt
def solution_5():
    print("\n\nSOLUTION 5: Shopping Receipt")
    print("-" * 50)
    item_name = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    
    subtotal = price * quantity
    
    # Determine discount
    if subtotal > 100:
        discount_rate = 0.10
    else:
        discount_rate = 0.05
    
    discount = subtotal * discount_rate
    tax = (subtotal - discount) * 0.08
    total = subtotal - discount + tax
    
    print(f"\n----- RECEIPT -----")
    print(f"Item: {item_name}")
    print(f"Price: ${price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: ${discount:.2f} ({discount_rate*100:.0f}%)")
    print(f"Tax: ${tax:.2f} (8%)")
    print(f"Total: ${total:.2f}")
    print(f"-------------------")


# SOLUTION 6: BMI Calculator
def solution_6():
    print("\n\nSOLUTION 6: BMI Calculator")
    print("-" * 50)
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    
    bmi = weight / (height ** 2)
    
    # Determine category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    print(f"Your BMI: {bmi:.1f}")
    print(f"Category: {category}")


# SOLUTION 7: Time Converter
def solution_7():
    print("\n\nSOLUTION 7: Time Converter")
    print("-" * 50)
    total_seconds = int(input("Enter seconds: "))
    
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    print(f"{total_seconds} seconds = {hours}:{minutes:02d}:{seconds:02d}")


# SOLUTION 8: Compound Interest Calculator
def solution_8():
    print("\n\nSOLUTION 8: Compound Interest Calculator")
    print("-" * 50)
    principal = float(input("Principal amount: "))
    rate = float(input("Annual interest rate (%): "))
    years = float(input("Number of years: "))
    
    final_amount = principal * ((1 + rate/100) ** years)
    interest = final_amount - principal
    
    print(f"Final amount: ${final_amount:.2f}")
    print(f"Interest earned: ${interest:.2f}")


# Uncomment the solution you want to test
# solution_1()
# solution_2()
# solution_3()
# solution_4()
# solution_5()
# solution_6()
# solution_7()
# solution_8()
