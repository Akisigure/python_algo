a,b = map(int,input().split())

while a >= b and a % 2 == 0:
    print(a, end=' ')
    a -= 2
    