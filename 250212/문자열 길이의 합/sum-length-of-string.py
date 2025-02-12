n = int(input())
cnt = 0
total_length = 0
for i in range(n):
    c = input()
    if c[0] == 'a':
        cnt += 1
    total_length += len(c)

print(total_length, cnt)

