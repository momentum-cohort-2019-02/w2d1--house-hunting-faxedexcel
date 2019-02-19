# Hard Mode:

annual_salary = input("Enter your annual salary: ")
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
r = input("Enter the expected annual rate of return [0.04]: ")
total_cost = input("Enter the cost of your dream home: ")
percent_down_payment = input("Enter the percent of your home's cost to save as a down payment [0.25]: ")

if percent_down_payment == "":
    percent_down_payment = 0.25 # default salary saving rate is 25%

portion_down_payment = float(total_cost) * float(percent_down_payment)

if r == "":
    r = 0.04 # default interest rate on savings is 4%

current_savings = 0
number_of_months = 0

while current_savings < portion_down_payment:
    current_savings += current_savings * float(r) / 12 # interest on savings
    current_savings += int(annual_salary) / 12 * float(portion_saved) # monthly savings from salary
    number_of_months += 1

print("Number of months:", number_of_months)

# Enter your annual salary: 80000
# Enter the percent of your salary to save, as a decimal: .15
# Enter the expected annual rate of return [0.04]: .05
# Enter the cost of your dream home: 500000
# Enter the percent of your home's cost to save as a down payment [0.25]: .2
# Number of months: 84