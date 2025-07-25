# temperature conversion tool

# global variables
# C = (F - 32) * 5/9
# F = C * 9/5 + 32

FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_fahrenheit(celsius):
    # F = C * 9/5 + 32
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def convert_to_celsius(fahrenheit):
    # C = (F - 32) * 5/9
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def main():
    temp_input = float(input("Enter the temperature to convert: "))
    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit_input == "F":
        converted_temp = convert_to_celsius(temp_input)
        print(f"{temp_input}F is {converted_temp}C")
    elif unit_input == "C":
        converted_temp = convert_to_fahrenheit(temp_input)
        print(f"{temp_input}C is {converted_temp}F")
    else: 
        #handle invalid input
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()

