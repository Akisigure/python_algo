from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
dxy = [[0,1],[0,-1],[1,0],[-1,0]]
visited = [[False] * n for _ in range(n)]

cnt = 0

def bfs(_x,_y):
    queue = deque([(_x,_y)])
    visited[_x][_y] = True

    while queue:
        x,y = queue.popleft()

        for dx,dy in dxy:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = True


for i in range(k):
    x,y = points[i]
    x -= 1
    y -= 1
    bfs(x,y)

for i in range(n):
    for j in range(n):
        if visited[i][j] == True:
            cnt += 1

print(cnt)