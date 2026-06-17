### Write a programe to calculate the percentage of student based on marks of any 5 subject.

## 1) Take Values:
 
#(m1,m2,m3,m4,m5) = (95,86,58,78,59)

# Perform opeations:

#obtained_marks = m1+m2+m3+m4+m5
#percentage = (obtained_marks / 500 * 100)

# Display Result:

#print('Percentage of Students is ', percentage)


## 2) Take input from User...

Total_marks = 500

# Take input from user 

Sub_1 = int(input('Enter marks of Subject 1 is : '))
Sub_2 = int(input('Enter marks of Subject 2 is : '))
Sub_3 = int(input('Enter marks of Subject 3 is : '))
Sub_4 = int(input('Enter marks of Subject 4 is : '))
Sub_5 = int(input('Enter marks of Subject 5 is : '))

# perform operation:

obtain_marks = (Sub_1 + Sub_2 + Sub_3 + Sub_4 + Sub_5)

Percentage = (obtain_marks / Total_marks * 100)

# Display Result :

print('Percentage of student of all 5 subject is : ', Percentage)








