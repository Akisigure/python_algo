n = int(input())
x = 65

for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    
    for j in range(n - i):
        print(chr(x),end=' ')
        x += 1
        if x == ord('['):
            x = 65
    print()