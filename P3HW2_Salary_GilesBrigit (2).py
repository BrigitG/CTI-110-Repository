# CTI-110
# P3HW2 - Salary
# Brigit Giles
# 3/20/2023
# Ask user to enter name of employee and store it in a variable
name = (input("Enter employee's name: "))
# Ask user to enter number of hours worked by employee and store it in a variable
hours = int(input('Enter number of hours worked: '))
# Ask user to enter employee's pay rate and store it in a variable
payRate = float(input("Enter employee's pay rate: "))
#process
otPayRate = payRate * 1.5
if hours > 40:
    ot = hours - 40
    otPay = ot * otPayRate
else:
    ot = 0
    otPay = 0
if hours <= 40:
    regPay = hours * payRate
else:
    regPay = (hours - ot) * payRate
gross = otPay + regPay

# Display employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay
print()
print('--------------------------------------------------')
print('Employee Name:  ',name)
print()
print('Hours Worked   Pay Rate   OverTime    OverTime Pay       Regular Pay      Gross Pay')
print('--------------------------------------------------------------------------------------')
print(f'     {hours}          {payRate:.2f}        {ot}         ${otPay:.2f}            ${regPay:.2f}         ${gross:.2f}')
