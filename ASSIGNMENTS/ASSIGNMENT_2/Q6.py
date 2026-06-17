### WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic. 

# Take input Basic salary from user

Basic = float(input('Enter Basic Salary : '))

# Perform Calculation

DA = ( 10 * Basic ) / 100
TA = ( 12 * Basic ) / 100
HRA = ( 15 * Basic ) / 100

Total_Salary = Basic + DA + TA + HRA 

# Display Result

print('DA is :', DA)
print('TA is : ', TA)
print('HRA IS : ', HRA)
print('Total salary is :', Total_Salary)