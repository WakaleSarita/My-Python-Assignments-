### 3. Accept no. of passengers from user and per ticket cost. Then accept age of each  
### passenger and then calculate total amount to ticket to travel for all of them based on following condition :  
#  a. Children below 12 = 30% discount  
#  b. Senior citizen (above 59) = 50% discount  
#  c. Others need to pay full. 


## Using While loop 

# p = int(input("Enter number of passanger: "))
# cost = int(input('Enter ticket cost : '))
# total = 0
# i = 1
# while i <= p:
#     age =  int(input(f'Enter age of passanger{i}: '))
#     if age < 12: total += cost * 0.7
#     elif age > 59: total += cost * 0.5
#     else: total += cost
#     i += 1
# print('Total =', total)

## Using for loop

p = int(input("Enter number of passanger: "))
cost = int(input('Enter ticket cost : '))
total = 0
for i in range(1, p+1):
    age =  int(input(f'Enter age of passanger{i}: '))
    if age < 12: total += cost * 0.7
    elif age > 59: total += cost * 0.5
    else: total += cost

print('Total =', total)