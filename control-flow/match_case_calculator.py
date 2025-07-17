# simple calculator with match case
# prompt for user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# choose type of operator
operations = input("Choose the operation (+, -, *, /)")

# conditions using match case
match operations:
    case "+":
        sum = num1 + num2
        print(f"The result is {sum}")
    case "-":
        difference = num1 - num2
        print(f"The result is {difference}")
    case "*":
        multiplication = num1 * num2
        print(f"The result is {multiplication}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            division = num1 / num2
            print(f"The result is {division}")
        
    case _:
        print("Invalid operations")
    
