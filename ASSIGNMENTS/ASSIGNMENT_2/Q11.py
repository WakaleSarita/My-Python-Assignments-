### Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

# Take input from user.

amount = int(input(' ENTER AMOUNT : '))

notes = [ 2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
total_notes = 0

# Perform operations and display result.

for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        total_notes += count
        print(note, 'X', count)
print('Total notes = ', total_notes)        
