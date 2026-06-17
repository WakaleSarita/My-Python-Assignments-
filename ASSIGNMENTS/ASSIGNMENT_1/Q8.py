### Write a Programe to convert days into years, weeks, and days. 

# Take input for users

Days = int(input(' Enter Days : '))

# Calculate the value years and days 

Year = Days // 365
Days = Days % 365

# Calulate the  values Weeks and days

Weeks = Days // 7
Days = Days % 7

# Display result 

#print(' Year is :', Year)

#print(' Weeks is : ', Weeks)

#print(' Dayss is : ', Days)

# or

print(f' YEARS:{Year}, WEEKS:{Weeks} , DAYS:{Days} ')






