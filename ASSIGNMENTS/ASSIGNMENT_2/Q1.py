### Convert the time entered in hh, min, and sec into seconds.

## Take input from user.

Hours = int(input(' Enter Hours : '))
Minutes = int(input(' Enter Minutes : '))
Seconds = int(input(' Enter Seconds : '))

# Calculate the total seconds

Total_Seconds = Hours * 3600 + Minutes * 60 + Seconds

# Display Result

print('Total Seconds : ', Total_Seconds)