### Write a program to calculate profit or loss.

 # Take input from user.

cost_price = float(input('Enter Cost Price is : '))
Selling_price = float(input('Enter Selling Price is : '))

amt = Selling_price - cost_price

# perform condition

if(amt > 0):
    print(amt, ' is the profit.')
elif(amt <= 0):
    print(amt, 'no profit or loss')
else:
    print(amt, ' is the loss')