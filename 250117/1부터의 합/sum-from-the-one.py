a = int(input())
cnt = 0
n = 0
for i in range(1,101):
    cnt += 1
    n += i
    if n >= a:
        break
print(cnt)
    