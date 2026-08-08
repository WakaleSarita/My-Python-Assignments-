# f.

# 1 2 3 4 5 
# 1     4   
# 1   3     
# 1 2       
# 1     

n = 5
for i in range(1, n+1):
    for j in range(1, n + 1):
        if i == 1 or j == 1 or j == n - i + 1:
            print(j, end = ' ')
        else:
            print(' ', end = ' ')
    print()