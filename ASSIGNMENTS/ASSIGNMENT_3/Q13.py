###  Write a program to input electricity unit charges and calculate total electricity bill 
#    according to the given condition: 
#    For first 50 units Rs. 0.50/unit 
#    For next 100 units Rs. 0.75/unit 
#    For next 100 units Rs. 1.20/unit 
#    For unit above 250 Rs. 1.50/unit 
#    An additional surcharge of 20% is added to the bill.

# Take inputs from user.

units = int(input('Enter total units consumed : '))
amount = 0

# Perform condition

if units <= 50:
    amount = units * 0.50
elif units <= 150:     # 50 + 100
    amount = ( 50 * 0.50 ) + (units - 50) * 0.75
elif units <= 250:     # 50 + 100 + 100
    amount = (50 * 0.50) + (100 * 0.75) + (units - 150) * 1.20
else:   # above 250
    amount = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (units -250) * 1.50

surcharge = amount * 0.20
total_bill = amount + surcharge

# Display result.

print(f'\nElectricity Bill : ')
print(f'Base Amount : Rs.{amount}')
print(f'surcharge 20%: Rs.{surcharge}')
print(f'Total Bill: Rs.{total_bill}')



