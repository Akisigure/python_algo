n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if j % 2 == 0:
            arr[i][j] = (n*2)*(j//2)+i
        else:
            arr[i][j] = (n*2)*((j-1)//2) + (2*n-1-i)

for row in range(n):
    for col in range(m):
        print(arr[row][col], end = ' ')
    print()
