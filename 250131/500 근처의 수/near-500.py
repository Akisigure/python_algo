import sys

r_num = 500
max_value = sys.maxsize
min_value = -sys.maxsize
max_temp = []
min_temp = []
arr = list(map(int,input().split()))

for i in arr :
    if i > r_num :
        max_temp.append(i)
    if i < r_num :
        min_temp.append(i)

for i in max_temp :
    if i < max_value :
        max_value = i

for i in min_temp :
    if i > min_value :
        min_value = i
        

print(min_value,max_value)     
