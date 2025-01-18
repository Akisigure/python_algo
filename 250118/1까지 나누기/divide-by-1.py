a = int(input())
cnt = 0
i = 1

while a >= 1:
    a = a // i
    i += 1
    cnt += 1

print(cnt)

