calculator = {
    "add": lambda x, y: x + y,  # Addition
    "subtract": lambda x, y: x - y,  # Subtraction
    "multiply": lambda x, y: x * y,  # Multiplication
    "divide": lambda x, y: x / y if y != 0 else "Division by zero error",  # Division
    "modulus": lambda x, y: x % y if y != 0 else
    "Division by zero error",  # Modulus
    "power": lambda x, y: x ** y,  # Power
    "floor_divide": lambda x, y: x // y if y != 0 else "Division by zero error"  # Floor Division
}

def calculate(operation, x, y):
    if operation in calculator:
        return calculator[operation](x, y)
    else:
        return "Invalid operation"
def main():
    print("Available operations: add, subtract, multiply, divide, modulus, power, floor_divide")
    operation = input("Enter the operation you want to perform: ").strip().lower()
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    
    result = calculate(operation, x, y)
    print(f"The result of {operation} between {x} and {y} is: {result}")

main()