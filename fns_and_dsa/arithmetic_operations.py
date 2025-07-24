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
        # check fo divide by zero scenario
        if num2 == o: 
            return f"Error! Cannot divide by zero" # return for divide by zero scenario
        return num1 / num2 # return for not divide by zero
    else:
        return f"Invalid operation"
    

       
