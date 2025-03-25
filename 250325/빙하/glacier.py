from collections import deque

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

dxy = [[0,1],[1,0],[0,-1],[-1,0]]


def bfs(_x,_y):
    visited = [[False] * m for _ in range(n)]
    queue = deque([(_x,_y)])
    visited[_x][_y] = True

    while queue:
        x,y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = True

    return visited


def ice():

    global arr
    time = 0
    last_cnt = 0

    while True:
        visited = bfs(0,0)
        ice_list = []

        cnt = sum(row.count(1) for row in arr)
        if cnt == 0:
            return time, last_cnt

        last_cnt = cnt

        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    water = 0
                    for dx,dy in dxy:
                        nx = dx + i
                        ny = dy + j

                        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                            water += 1
                    if water > 0:
                        ice_list.append((i,j))

        for x, y in ice_list:
            arr[x][y] = 0

        time += 1


time,last_cnt = ice()
print(time,last_cnt)