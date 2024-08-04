import inspect

def add(a, b):
    result = a + b
    print(f"a + b = {result}")

def sub(a, b):
    result = a - b
    print(f"a - b = {result}")

def mul(a, b):
    result = a * b
    print(f"a * b = {result}")

def div(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = a / b
        print(f"a / b = {result}")

def print_stack():
    print("Current stack trace:")
    stack = inspect.stack()
    for frame in stack:
        print(f"File: {frame.filename}, Line: {frame.lineno}, Function: {frame.function}")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")

print_stack()  # Print the stack trace here

if op == "+":
    add(a, b)
elif op == "-":
    sub(a, b)
elif op == "*":
    mul(a, b)
elif op == "/":
    div(a, b)
else:
    print("Invalid operator")

