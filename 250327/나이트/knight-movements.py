from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dxy = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,-2],[2,-1],[2,1],[1,2]]


def bfs(_x,_y,dep):

    queue = deque([(_x,_y,dep)])
    global res

    while queue:
        x,y,depth = queue.popleft()

        if arr[x][y] == -1:
            res = depth
            break

        for dx,dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny,depth + 1))


# Please write your code here.
arr = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
arr[r1 - 1][c1 - 1] = 1
arr[r2 - 1][c2 - 1] = -1
res = -1

visited[r1 - 1][c1 - 1] = True

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bfs(i,j,0)

print(res)