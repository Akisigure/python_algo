import sys

n = int(input())
a = list(map(int, input().split()))

min_val = sys.maxsize
# Write your code here!

for i in range(n):
    if min_val > a[i] :
        min_val = a[i]

cnt = a.count(min_val)
print(min_val,cnt)