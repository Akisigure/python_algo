n = int(input())
# x1 y1 x2 y2
arr = [[0] * 201 for _ in range(201)]
cnt = 0
for i in range(n):
    a,b,c,d = map(int,input().split())
    a += 100
    b += 100
    c += 100
    d += 100
    for j in range(a,c):
        for k in range(b,d):
            arr[j][k] += 1

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] >= 1:
            cnt += 1

print(cnt)

