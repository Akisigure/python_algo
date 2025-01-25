n = int(input())
a = 11
b = a
cnt = 0

for i in range(n):
    for j in range(n):
        print(a,end=' ')
        cnt += 1
        a += 2
        if cnt == 1:
            b = a
    print()
    cnt = 0
    a = b
    
        