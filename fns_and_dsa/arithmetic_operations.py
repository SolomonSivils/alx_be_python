# function for basic arithmetic

def perform_operation(num1, num2, operation):
    operation = "add", "subtract", "multiply", "divide"
    if num2 == 0:
        return f"Cannot divide by zero"
    return operation
