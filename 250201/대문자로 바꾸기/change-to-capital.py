n = 5

arr = [list(input().split()) for _ in range(n)]

for i in range(n):
    for j in range(3):
        arr[i][j] = arr[i][j].upper()
        print(arr[i][j],end=' ')
        if j >= 2:
            print()
