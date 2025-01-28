n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    s = 1

    for j in range(a,b+1):
        s = s * j
    print(s)

        
        
