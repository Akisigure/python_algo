n = int(input())

a = 9
    
for i in range(n):
    for j in range(n):
        a += 2
        print(a, end=' ')
    print()
    a -= 8