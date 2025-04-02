n, m = map(int,input().split())

node = [0] * (n + 1)


def make_set(x):
    node[x] = x


def find_set(x):
    if node[x] != x:
        node[x] = find_set(node[x])
    return node[x]


def union(x,y):
    px = find_set(x)
    py = find_set(y)
    if px != py:
        if px < py:
            node[py] = px
        else:
            node[px] = py


for k in range(1, n + 1):
    make_set(k)


for i in range(m):
    cnt = 0
    lst = list(input().split())

    if lst[0] == 'x':
        a, b = int(lst[1]),int(lst[2])
        union(a,b)
    if lst[0] == 'y':
        val = int(lst[1])
        root = find_set(val)

        for v in range(1, n + 1):
            find_set(v)
        cnt = node.count(root)
        print(cnt)

