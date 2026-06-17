### Convert Distance given in feet and inches into meter and centimeter.

## 1 foot = 12 inches
## 1 inch = 2.54 cm
## 100 cm = 1 meter 

# Input values from user

Feet = float(input('Enter feet : '))
Inches = float(input('Enter inches : '))

# Convert feet and inches into total inches.

Total_inches = Feet * 12 + Inches

# Convert inches into centimeters.

Total_cm = Total_inches * 2.54

# convert meter and centimeters.

Meters = Total_cm // 100
Centimeters = Total_cm % 100

# Display Result 

print('Distant into meter is : ' , Meters)
print('Distant into centimeters is : ', Centimeters)







