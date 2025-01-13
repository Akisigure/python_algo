a,b = input().split()

b = int(b)

if 'A' == a:
    for i in range(1,b+1):
        print(i, end=' ')
elif 'D' == a :
    for i in range(b,0,-1):
        print(i, end=' ')