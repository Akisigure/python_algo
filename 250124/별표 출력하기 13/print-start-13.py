n = int(input())

x = 1
y = n

for i in range(n * 2):
    if i % 2 != 0:
        for _ in range(x):
            print('*',end=' ')
        print()
        x += 1
        
    else :
        for _ in range(y):
            print('*', end=' ')
        print()
        y -= 1
        