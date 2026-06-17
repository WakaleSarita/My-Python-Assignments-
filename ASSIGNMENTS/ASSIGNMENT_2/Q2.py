### Convert temp from Celsius to Fahrenheit. (C/5 =( F-32)/9)

## F = (c * 9/5 ) + 32

# Input Temperature in Celsius From users.
# float() is used because temperature can have decimal values 
# if we use int() , Python only accepts whole numbers.

Celsius = float(input('Enter temperature in Celsius : '))

# Convert to Fahrenheit.

Fahrenheit = (Celsius * 9 / 5 ) + 32

# Display Result.

print('Temperature in Fahrenheit is : ', Fahrenheit)
