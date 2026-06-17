### Write a program to input angles of a triangle and check whether triangle is valid or not.

# Take input from user.

Angle_1 = int(input('Enter angle first : '))
Angle_2 = int(input('Enter angle second : '))
Angle_3 = int(input('Enter angle third: '))

# Perform condition

if(Angle_1 + Angle_2 + Angle_3 == 180):
    print('Angle of traingle is valid.')
else:
    print('Angle of traingle is not valid. ')

