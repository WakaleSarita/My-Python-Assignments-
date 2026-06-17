### WAP to calculate area of triangle and rectangle. 

## Area of Triangle = 1/2 * b* h     ( b= Breadth , h = Height)
## Area of Rectangle = l * b          (l = Length)

# Take input from user.

length = float(input('Enter Length : '))
breadth = float(input('Enter breadth : '))
height = float(input('Enter height : '))

# Perform operations

Area_T = 1 / 2 * breadth * height
Area_R = length * breadth

# Display result

print('Area of Triangle is : ', Area_T)
print('Area of Rectangle is : ', Area_R)