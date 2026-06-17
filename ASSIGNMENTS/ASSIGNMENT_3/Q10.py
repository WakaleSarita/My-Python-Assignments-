### Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18).

# Take input from user 

gender = input ('Enter gender(M/F) : ')
age = int(input ('Enter age :'))

# Perform condition with display result 

if(gender == 'F'):
    if(age >= 18):
        print('Girl is eligible for marriage .')
    else:
        print('pehle bade ho jao.')
else:
    if(age >= 21):
        print('Boy is eligible for marriage.')
    else:
        print('pehle kama lo.')