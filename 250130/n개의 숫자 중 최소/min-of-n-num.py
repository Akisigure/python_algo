import sys

n = int(input())
a = list(map(int, input().split()))

min_val = sys.maxsize
cnt = 0
# Write your code here!

for i in range(n):
    if min_val > a[i] :
        min_val = a[i]
        if min_val == a[i] :
            cnt += 1
    
print(min_val,cnt)