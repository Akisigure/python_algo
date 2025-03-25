from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
row, col = map(int, input().split())
row -= 1
col -= 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start_x, start_y):
    x, y = start_x, start_y

    for _ in range(k):
        queue = deque([(x, y)])
        max_value = -1
        next_positions = []

        while queue:
            cur_x, cur_y = queue.popleft()

            for i in range(4):
                nx, ny = cur_x + dx[i], cur_y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] < arr[x][y]:
                    if arr[nx][ny] > max_value:
                        max_value = arr[nx][ny]
                        next_positions = [(nx, ny)]
                    elif arr[nx][ny] == max_value:
                        next_positions.append((nx, ny))

        if not next_positions:
            break

        next_positions.sort()
        x, y = next_positions[0]

    return x, y


final_row, final_col = bfs(row, col)
print(final_row, final_col)
