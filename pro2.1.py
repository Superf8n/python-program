#2.1 Program to demonstrate basic exception handling in Python

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numeric values.")

finally:
    print("Program execution completed.")
