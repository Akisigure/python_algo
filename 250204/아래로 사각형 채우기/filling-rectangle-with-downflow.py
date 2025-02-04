n = int(input())

num = 1
arr = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if j == 0 :
            num = i + 1
        arr[i][j] = num
        num += n
        print(arr[i][j],end=' ')
    print()