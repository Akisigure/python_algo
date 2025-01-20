a = int(input())
cnt = 0

while True:
    if a >= 1000 :
        break
    if a % 2 == 0 :
        a = a * 3 + 1
        cnt += 1
    elif a % 2 != 0:
        a = a * 2 + 2
        cnt += 1

print(cnt)
    