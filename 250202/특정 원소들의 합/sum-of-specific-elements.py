n = 4
arr = [list(map(int,input().split())) for i in range(n)]
s = 0

for i in range(n):
    for j in range(i + 1):
        s += arr[i][j]

print(s)