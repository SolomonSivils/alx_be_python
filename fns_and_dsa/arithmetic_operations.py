# function for basic arithmetic

def perform_operation(num1, num2, operation):
    operation = "add", "subtract", "multiply", "divide"
    if operation == "add": # condition
        return num1 + num2 # implementation of an operation choosen
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == o: # divide by zero scenario
            return f"Error! Cannot divide by zero"
        return num1 / num2
    else:
        return f"Invalid operation"
    

       
