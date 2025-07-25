# datetime module
# part 1
# import datetime
import datetime


# function display current datetime

current_date = datetime.datetime.now() # global
def display_current_datetime():
    # format and print current date and time as "YYYY-MM-DD HH:MM:SS"
    formated_date = current_date.strftime("%y-%m-%d %H:%M:%S")
    print (f"Current date and time: {formated_date}")

display_current_datetime()

# part 2: calculate a future date
# prompt the user to enter a number of days (as an integer)


from datetime import timedelta

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    days_to_add = timedelta(days=number_of_days)
    future_date = current_date + days_to_add
    formated_future_date = future_date.strftime("%y-%m-%d %H:%M:%S")
    print(f"Future date: {formated_future_date}") 

calculate_future_date()