# function for basic arithmetic

def perform_operation(num1: float, num2: float, operation: str):
    operation = "add", "subtract", "multiply", "divide"
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return f"Cannot divide by zero"
            else:
                return num1 / num2
        case _:
            return f"Invalid operation"
    return operation
