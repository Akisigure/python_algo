arr = list(map(int,input().split()))
s = 0
cnt = 0

for i in arr :
    if i == 0:
        break
    else :
        s += i
        cnt += 1

avg = s / cnt
print('%d %.1f' %(s,avg))



