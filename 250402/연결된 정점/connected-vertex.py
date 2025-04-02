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

    if node[px] > node[py]:
        node[px] = py
    if node[px] < node[py]:
        node[py] = px


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
        # for v in range(len(node)):
        #     find_set(v)
        for j in range(len(node)):
            if node[j] == val:
                cnt += 1
        print(cnt)
