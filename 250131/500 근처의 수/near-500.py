import sys

r_num = 500
max_value = sys.maxsize
min_value = sys.maxsize
temp = []

arr = list(map(int,input().split()))

for i in arr :
    if i > r_num :
        temp.append(i)
    if i < r_num :
        min_value = i

for i in temp :
    if i < max_value :
        max_value = i
        

print(min_value,max_value)     
