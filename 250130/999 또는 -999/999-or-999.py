import sys

arr = list(map(int,input().split()))
max_val = -sys.maxsize
min_val = sys.maxsize

for i in arr :
    if i == -999 or i == 999 :
        break
    
    if i > max_val :
        max_val = i
    if i < min_val :
        min_val = i

print(max_val,min_val)
