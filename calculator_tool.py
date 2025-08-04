def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

# Optional test block
if __name__ == "__main__":
    print("Add:", add(3, 5))         # 8
    print("Subtract:", subtract(10, 4))  # 6
    print("Multiply:", multiply(4, 6))  # 24
    print("Divide:", divide(8, 2))      # 4.0
    print("Divide by zero:", divide(5, 0))  # Error