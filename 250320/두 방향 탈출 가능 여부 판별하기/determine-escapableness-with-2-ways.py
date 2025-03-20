dxy = [[1,0],[0,1]]

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

res = 0


def dfs(x,y):

    global res

    if x == n - 1 and y == m - 1:
        res = 1
        return

    if visited[x][y]:
        return

    visited[x][y] = True

    for dx,dy in dxy:
        nx = dx + x
        ny = dy + y

        if 0 <= nx < n and 0 <= ny < m   and arr[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)


dfs(0,0)
print(res)