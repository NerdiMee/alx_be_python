monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
rate = 0.05

projected_annual_savings = monthly_savings + 12 * int(monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}")