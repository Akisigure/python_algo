from collections import deque

n, m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dxy = [[0,1],[0,-1],[1,0],[-1,0]]
res = 0


def bfs(_x,_y):
    queue = deque([(_x,_y)])
    visited[_x][_y] = True

    global res

    while queue:
        x,y = queue.popleft()

        if x == n - 1 and y == m - 1:
            res = 1
            break

        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                queue.append((nx,ny))
                visited[nx][ny] = True


bfs(0,0)
print(res)

