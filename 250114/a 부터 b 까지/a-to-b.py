a,b = map(int,input().split())

for _ in range(a,b+1):
    if a > b:
        break
    if a % 2 == 0:
        print(a, end=' ')
        a += 3
    else :
        print(a, end=' ')
        a *= 2