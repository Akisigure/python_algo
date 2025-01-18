a = int(input())
cnt = 0
i = 0

while a >= 1:
    i += 1
    a = a // i
    cnt += 1
    if 1 >= a:
        break

print(cnt)

