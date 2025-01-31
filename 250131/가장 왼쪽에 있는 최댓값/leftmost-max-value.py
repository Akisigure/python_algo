import sys

n = int(input())
a = list(map(int, input().split()))

max_value = -sys.maxsize
t = [0] * n
# Write your code here!
for i in range(n):
    if a[i] > max_value :
        max_value = a[i]
        t[i] = i + 1

for i in t[::-1]:
    if i == 0:
        continue
    
    print(i,end=' ')