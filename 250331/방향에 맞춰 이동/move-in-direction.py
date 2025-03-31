n = int(input())
start = [0,0]
for i in range(n):
    arr = list(map(str,input()))
    target = arr[0]
    num = arr[2]
    num = int(num)

    if target == 'N':
        start[1] += num
    if target == 'E':
        start[0] += num
    if target == 'S':
        start[1] -= num
    if target == 'W':
        start[0] -= num

print(*start)