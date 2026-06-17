### Find the sum of three-digit number.

# Take input From user 

#num = int(input('Enter three digit number : '))

# perform operation

#d1 = num % 10
#num = num // 10

#d2 =num % 10
#num = num // 10

#d3 = num % 10
#num = num // 10

#sum = d1 + d2 + d3 

# Display Result

#print('d1 is' , d1)
#print('d2 is' , d2)
#print('d3 is' , d3)
#print('Sum of three digits is: ', sum)



# Or

# Take input From user 

num = int(input('Enter three digit number : '))

# Extract digits
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

Sum_digits = hundreds + tens + units

# Display result

print('Sum of three digits is: ', Sum_digits)




