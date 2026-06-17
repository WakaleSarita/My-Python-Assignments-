### Input 5 subject marks from user and display grade(eg.First class,Second class ..) 

# Take input valuse for Users

S_1 = int(input('Enter marks for subject 1 : '))
S_2 = int(input('Enter marks for subject 2 : '))
S_3 = int(input('Enter marks for subject 3 : '))
S_4 = int(input('Enter marks for subject 4 : '))
S_5 = int(input('Enter marks for subject 5 : '))

# calculate total marks

Total = S_1 + S_2 + S_3 + S_4 + S_5 
print('Total : ', Total)

#  calculate Percentage

Percentage = Total / 5
print('Percentage :', Percentage)

# Apply conditions and Display result

if Percentage >= 70:
    print('First Class')
elif Percentage >= 60:
    print(' Second Class')
elif Percentage  >= 50:
    print('Third class')
elif Percentage >= 35:
    print('Pass Class')
else:
    print('FAIL')