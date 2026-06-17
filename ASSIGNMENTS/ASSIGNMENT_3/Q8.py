### Write a program to prompt user to enter userid and password. After verifying 
### userid and password display a 4 digit random number and ask user to enter the 
### same. If user enters the same number then show him success message otherwise 
### failed. (Something like captcha)


import random 

# Take Values
User_name = "Sarita"
Pass_word = "12345"

# Take input from user.

userid = input('Enter UserId : ')
password = input('Enter password : ') 

# perform condition

if(userid == User_name and password == Pass_word):
    print('Login Successful!')

    # generate a random verification number

    random_number = random.randint(1000, 9999)
    print('Verification Number :' , random_number)

    # Ask user to enter the same number
    user_number = int(input('Enter the same number : '))

    # Verify the number

    if user_number == random_number:
        print('User Verification Successful. ')
    else:
        print('Verification Failed.')
else:
    print('Invalid User ID or Password.')


   

