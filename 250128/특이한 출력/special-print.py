n = int(input())
s = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        s = i + j
        if s % 4 == 0 :
            print(f'{(i, j)}')
        else :
            print(f'{(i, j)}',end=' ')