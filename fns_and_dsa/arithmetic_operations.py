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
        # handling for division by zero, returning a specific message or value that your main.py script can recognize and display appropriately.
        if num2 == 0: 
            return f"Error! Cannot divide by zero" # return for divide by zero scenario
        else:
            return num1 / num2 # return for not divide by zero
    else:
        return f"Invalid operation"
    

       
