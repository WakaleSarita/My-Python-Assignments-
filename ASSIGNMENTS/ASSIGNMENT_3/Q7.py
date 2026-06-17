### Write a program to check if user has entered correct userid and password. 

# Take valuse

username = 'Sarita'
password = '12345'

# Take input from user

User_Id = input('ENTER USERNAME : ' )
pass_Id = input('ENTER PASSWORD : ' )

# perform condition

if (username == User_Id and password == pass_Id ):
    print('Log in successful')
else:
    print('Invalid Creditentional')