n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

visited = [[False] * n for _ in range(n)]
# Please write your code here.
human = 0
human_lst = []


def dfs(x, y):

    visited[x][y] = True

    size = 1

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
            size += dfs(nx, ny)

    return size


cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            cnt += 1
            human_lst.append(dfs(i,j))

human_lst.sort()
print(cnt)
for i in human_lst:
    print(i)