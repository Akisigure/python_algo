n = int(input())
start = [0,0]
for i in range(n):
    arr = input().split()
    target = arr[0]
    num = int(arr[1])

    if target == 'N':
        start[1] += num
    if target == 'E':
        start[0] += num
    if target == 'S':
        start[1] -= num
    if target == 'W':
        start[0] -= num

print(*start)