# Function Addition
def add(a, b):
    return a + b

# Function subtraction
def subtract(a, b):
    return a - b

# Function Multiplication
def multiply(a, b):
    return a * b

# Function Divide
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"