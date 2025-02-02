a,b = map(int,input().split())

arr = [[0 for i in range(b)]
for i in range(a)]

num = 1

for i in range(a):
    for j in range(b):
        arr[i][j] = num
        num += 1
        print(arr[i][j],end=' ')
    print()