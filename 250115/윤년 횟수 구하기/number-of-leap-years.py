n = int(input())
cnt = 0
temp = 0
for i in range(1,n+1):
    if i % 100 == 0 and i % 400 != 0:
        temp += 1
    elif i % 4 == 0:
        cnt += 1

print(cnt) 
    