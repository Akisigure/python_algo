n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

mv = -1
for i in range(n):
    for j in range(n):
        v = 0

        for k in range(3):
            for l in range(3):
                x = i + k
                y = j + l

                if 0 <= x < n and 0 <= y < n:
                    if arr[x][y] == 1:
                        v += 1
        mv = max(mv,v)

print(mv)