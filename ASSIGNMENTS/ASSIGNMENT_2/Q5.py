### WAP to calculate selling price of book based on cost price and discount.

## Formula : 
## Discount Amount = (Cost Price * Discount '%') / 100
## Selling Price = Cost Price - Discount Amount 

# Take input from user

Cost_Price = float(input('Enter Cost price of the book : '))
Discount = float(input('Enter Discount Percentage : '))

# Calculate Discount Amount 

Discount_Amount = (Cost_Price * Discount ) / 100

# Calculate Selling price

Selling_Amount = Cost_Price - Discount_Amount 

# Display Result 

print('Selling Price of the book is : ', Selling_Amount)



