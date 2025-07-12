# calculate users monthly savings based on inputted income and expenses
# project savings over a year given a fixed interest rate

# prompt for monthly income
monthly_income = int(input("Enter your monthly income: "))

# prompt for expenses
monthly_expenses = int(input("Enter your total monthly expenses: "))

# calculate monthly savings (difference between monthly income and monthly expenses)
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are ${monthly_savings}")

# project annual savings
# assume annual interest rate of 5%
# calculate projected savings after one year incorporating the interes
# use formula (Projected Savings = Monthly Savings * 12 + (Monthly savings * 12 * 0.05))
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${projected_savings}")