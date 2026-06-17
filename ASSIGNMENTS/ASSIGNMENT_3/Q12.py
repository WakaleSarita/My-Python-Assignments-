### Write a program to check if given 3 digit number is a palindrome or not. 

# Take input from user.

num = int(input('Enter a 3 digits number : '))

#perform condition with results

if num < 100 or num > 999:
    print(' Please enter a only three digits number')
else:
    # 121     first digit = 1 , last digit = 1 
    first_digit = num // 100
    second_digit = num % 10 
    print('First digit : ', first_digit)
    print('Second digit :', second_digit)

    if first_digit == second_digit:
        #print('The given number is palindrome.')
        print(f'{num} is a palindrome number .')
    else:
        #print('The given number is not palindrome.')
        print(f'{num} is not palindrome number .')
