# multiplication table generator
# prompt user for a number
number = int(input("Enter a number to see its multiplication table: "))

# generate and print the multiplication table
for Y in range (1, 11):
    product = number * Y
    print(f"{number} * {Y} = {product}")