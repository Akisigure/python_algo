n = int(input())
x = 65

for i in range(1,n+1):
    for j in range(i):
        print(chr(x),end='')
        x += 1
        if x == ord('['):
            x = 65
    print()