a,b = map(int,input().split())
calc = 0
avg = 0.0
cnt = 0

for i in range(a,b+1):
    if i % 5 == 0 or i % 7 == 0:
        calc += i
        cnt += 1

avg = calc / cnt        
print("%d %.1f" %(calc,avg),end=' ')