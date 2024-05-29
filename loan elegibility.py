#enter the person's name, age, and annual income
name = input("Enter your name: ")
age = int(input("Enter your age: "))
annual_income = float(input("Enter your annual income: "))

# Loan eligibility criteria checks
required_age = 21
required_income = 21000

# Determine loan eligibility based on criteria
if age >= required_age and annual_income >= required_income:
    loan_status = "Loan Granted"
else:
    loan_status = "Loan Not Granted"

# Output loan status
print("{}: {}".format(name, loan_status))
