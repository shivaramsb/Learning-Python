"""
Day 1 Mini-Project: Advanced Calculator
Build a feature-rich calculator with multiple operations
"""

print("=" * 50)
print("      ADVANCED CALCULATOR".center(50))
print("=" * 50)

# Display menu
print("\nSelect an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Floor Division (//)")
print("6. Modulus (%)")
print("7. Exponent (**)")
print("8. Square Root")
print("9. Percentage")
print("0. Exit")

# Get user choice
choice = input("\nEnter choice (1-9, or 0 to exit): ")

# Exit if user chooses 0
if choice == "0":
    print("Thank you for using the calculator. Goodbye!")
    exit()

# Get numbers based on operation
if choice == "8":
    # Square root only needs one number
    num1 = float(input("Enter the number: "))
    num2 = None
elif choice == "9":
    # Percentage: What is X% of Y?
    num1 = float(input("Enter the percentage: "))
    num2 = float(input("Enter the number: "))
else:
    # All other operations need two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

# Perform calculation based on choice
print("\n" + "-" * 50)

if choice == "1":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif choice == "2":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif choice == "3":
    result = num1 * num2
    print(f"Result: {num1} × {num2} = {result}")

elif choice == "4":
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"Result: {num1} ÷ {num2} = {result:.4f}")

elif choice == "5":
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 // num2
        print(f"Result: {num1} // {num2} = {result}")

elif choice == "6":
    if num2 == 0:
        print("Error: Cannot perform modulus with zero!")
    else:
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")

elif choice == "7":
    result = num1 ** num2
    print(f"Result: {num1} ^ {num2} = {result}")

elif choice == "8":
    if num1 < 0:
        print("Error: Cannot calculate square root of negative number!")
    else:
        result = num1 ** 0.5
        print(f"Result: √{num1} = {result:.4f}")

elif choice == "9":
    result = (num1 / 100) * num2
    print(f"Result: {num1}% of {num2} = {result:.2f}")

else:
    print("Invalid choice! Please select a number from 1-9.")

print("-" * 50)


# ============================================
# BONUS: Enhanced Calculator with Loop
# ============================================
"""
Uncomment the code below for an enhanced version that:
- Runs in a loop until user chooses to exit
- Shows calculation history
- Handles errors gracefully
"""

"""
def enhanced_calculator():
    history = []
    
    while True:
        print("\n" + "=" * 50)
        print("      ENHANCED CALCULATOR".center(50))
        print("=" * 50)
        
        print("\nOperations:")
        print("1. Add (+)        2. Subtract (-)     3. Multiply (*)")
        print("4. Divide (/)     5. Floor Div (//)   6. Modulus (%)")
        print("7. Power (**)     8. Square Root      9. Percentage")
        print("10. View History  0. Exit")
        
        choice = input("\nEnter choice: ")
        
        # Exit
        if choice == "0":
            print("\nCalculation History:")
            if history:
                for i, calc in enumerate(history, 1):
                    print(f"{i}. {calc}")
            else:
                print("No calculations performed.")
            print("\nThank you for using the calculator!")
            break
        
        # View history
        if choice == "10":
            print("\nCalculation History:")
            if history:
                for i, calc in enumerate(history, 1):
                    print(f"{i}. {calc}")
            else:
                print("No calculations performed yet.")
            continue
        
        # Get inputs
        try:
            if choice == "8":
                num1 = float(input("Enter number: "))
                num2 = None
            elif choice == "9":
                num1 = float(input("Enter percentage: "))
                num2 = float(input("Enter number: "))
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter valid numbers!")
            continue
        
        # Perform calculations
        try:
            if choice == "1":
                result = num1 + num2
                calc_str = f"{num1} + {num2} = {result}"
            elif choice == "2":
                result = num1 - num2
                calc_str = f"{num1} - {num2} = {result}"
            elif choice == "3":
                result = num1 * num2
                calc_str = f"{num1} × {num2} = {result}"
            elif choice == "4":
                result = num1 / num2
                calc_str = f"{num1} ÷ {num2} = {result:.4f}"
            elif choice == "5":
                result = num1 // num2
                calc_str = f"{num1} // {num2} = {result}"
            elif choice == "6":
                result = num1 % num2
                calc_str = f"{num1} % {num2} = {result}"
            elif choice == "7":
                result = num1 ** num2
                calc_str = f"{num1} ^ {num2} = {result}"
            elif choice == "8":
                if num1 < 0:
                    raise ValueError("Cannot calculate square root of negative number")
                result = num1 ** 0.5
                calc_str = f"√{num1} = {result:.4f}"
            elif choice == "9":
                result = (num1 / 100) * num2
                calc_str = f"{num1}% of {num2} = {result:.2f}"
            else:
                print("Invalid choice!")
                continue
            
            print(f"\nResult: {calc_str}")
            history.append(calc_str)
            
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Run the enhanced calculator
# enhanced_calculator()
"""
