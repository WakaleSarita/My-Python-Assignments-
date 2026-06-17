###  Write a program to enter P , T , R and calculate Compound Interest.


# Compound Interes  = P( 1 + R/100)^T - P
# P = Principle Amount 
# R = Annual Interest Rate
# T = Time 
# CI = Compound Interests

# Take values for user.

P = int(input('Enter Priciple amount : '))
T = int(input('Enter Time : '))
R = int(input('Enter Annual Interest Rate : '))

# Perform Operation.

CI = P * 1 + R / 100 ** T - P 

# Display Result.

print('Compound Interest is : ', CI)
