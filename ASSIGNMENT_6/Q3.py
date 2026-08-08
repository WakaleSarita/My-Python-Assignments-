# c.

#         1   
#       1   1   
#     1   2   1   
#   1   3   3   1   

for i in range(4):
    for j in range(4 - i):
        print(' ', end= ' ')
    val = 1
    for j in range(i +1):
        print(val, end = '   ')
        val = val * (i-j) // (j+1)
    print()