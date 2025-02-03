n = 3
arr = []
arr2 = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
sp = input()
for _ in range(n):
    arr2.append(list(map(int,input().split())))

arr_s = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        arr_s[i][j] = arr[i][j] * arr2[i][j]
        print(arr_s[i][j],end=' ')
    print()