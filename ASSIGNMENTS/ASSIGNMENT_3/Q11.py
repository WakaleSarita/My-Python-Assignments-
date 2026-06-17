###  Accept age of five people and also per person ticket amount and then calculate total 
#    amount to ticket to travel for all of them based on following condition : 
#    a. Children below 12 = 30% discount 
#    b. Senior citizen (above 59) = 50% discount 
#    c. Others need to pay full. 


# Take input from user.

ticket_price = int(input('Enter ticket price per person: '))

age1 = int(input('Enter age of person 1 : '))
age2 = int(input('Enter age of person 2 : '))
age3 = int(input('Enter age of person 3 : '))
age4 = int(input('Enter age of person 4 : '))
age5 = int(input('Enter age of person 5 : '))

Total = 0

# Person 1

if age1 < 12:
    amount1 = ticket_price * 0.7             # 30 % discount.
elif age1 > 59:
    amount1 = ticket_price * 0.5             # 50 % discount.
else:
    amount1 = ticket_price

Total = Total + amount1


# Person 2

if age2 < 12:
    amount12 = ticket_price * 0.7             # 30 % discount.
elif age2 > 59:
    amount2 = ticket_price * 0.5             # 50 % discount.
else:
    amount2 = ticket_price

Total = Total + amount2


# Person 3

if age3 < 12:
    amount3 = ticket_price * 0.7             # 30 % discount.
elif age3 > 59:
    amount3 = ticket_price * 0.5             # 50 % discount.
else:
    amount3 = ticket_price

Total = Total + amount3


# Person 4

if age4 < 12:
    amount4 = ticket_price * 0.7             # 30 % discount.
elif age4 > 59:
    amount4 = ticket_price * 0.5             # 50 % discount.
else:
    amount4 = ticket_price

Total = Total + amount4


# Person 5

if age5 < 12:
    amount5 = ticket_price * 0.7             # 30 % discount.
elif age5 > 59:
    amount5 = ticket_price * 0.5             # 50 % discount.
else:
    amount5 = ticket_price

Total = Total + amount5


# Display Result.

print('Total amount for 5 people = ' , Total)
