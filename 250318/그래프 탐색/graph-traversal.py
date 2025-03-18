from collections import defaultdict

n, m = map(int, input().split())

graph = defaultdict(list)
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
cnt = 0


def dfs(root):

    global cnt
    if visited[root]:
        return

    visited[root] = True

    for ver in graph[root]:
        if not visited[ver]:
            cnt += 1
            dfs(ver)


dfs(1)
print(cnt)

