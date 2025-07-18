# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Ensure input is a positive integer
if size <= 0:
    print("Enter a positive integer")
else:
    row_count = 0 
    while row_count < size:
        for r in range(size): 
            print("*", end="") 
            
        print() 
        row_count += 1 

