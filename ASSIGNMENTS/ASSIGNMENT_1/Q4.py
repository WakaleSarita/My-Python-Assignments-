### Write a program to enter P , T , R and calculate simple interest.

# Simple Interest = P + T + R / 100
# P = Principle Amount 
# R = Annual Interest Rate
# T = Time 
# SI = Simple Interest

# Take values for user.

P = int(input('Enter Priciple amount : '))
T = int(input('Enter Time : '))
R = int(input('Enter Annual Interest Rate : '))

# Perform Operation.

SI = P * T * R / 100

# Display Result.

print('Simple Interest is : ', SI)

