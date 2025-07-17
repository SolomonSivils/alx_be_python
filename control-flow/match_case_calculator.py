# simple calculator with match case
# prompt for user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# input prompt for the operation
operation = input("Choose the operation (+, -, *, /): ")

# perform operations using match case

# initialize result to none
result = None

# match case statement for operations
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        # handle divisions by zero gracefully
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
        
    case _:
        print("Invalid operations")
    
