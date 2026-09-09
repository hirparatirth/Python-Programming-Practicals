# Accept two numbers from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform operations
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)

if b != 0:
    print("Division =", a / b)
else:
    print("Division is not possible by zero")