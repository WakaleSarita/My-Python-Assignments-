### 1. Write a program to prompt user to enter userid and password. If Id and  
### password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.  

## Using while loop 

# userid = 'Sarita'
# password = '954538'
# i = 0
# while i < 3:
#     u = input('Enter userid : ')
#     p = input('Enter password : ')
#     if u == userid and p == password:
#         print('Login Successful')
#         break
#     else:
#         print("Wrong. Attempts left: ", 2-i)
#         i += 1
# else:
#     print('Account Locked')


## Using For loop

userid = 'Sarita'
password = '954538'
for i in range(1,4):          # (3) , (1,4,1) chalel
    u = input('Enter userid : ')
    p = input('Enter password : ')
    if u == userid and p == password:
        print('Login Successful')
        break
    else:
        print("Wrong. Attempts left: ", 2-i)
        i += 1
else:
    print('Account Locked')
