start, end = map(int, input().split())
cnt = 0
s = 0
# Write your code here!
for i in range(start,end+1):
    s = 0
    
    for j in range(1,i):
        if i % j == 0:
            s += j
    if s == i:
        cnt += 1
                
    
print(cnt)
