n,m = map(int,input().split())

arr = []
arr2 = []

temp = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for _ in range(n):
    arr.append(list(map(int,input().split())))
    
for _ in range(n):
    arr2.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] != arr2[i][j] :
            temp[i][j] = 1
        print(temp[i][j],end=' ')
    print()
