a = int(input())
b = 1
cnt = 0
for i in range(1,11):
    b *= i
    cnt += 1
    if b >= a:
        break
print(cnt)
   