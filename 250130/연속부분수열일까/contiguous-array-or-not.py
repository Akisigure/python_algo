a,b = map(int,input().split())
a_arr = list(map(int,input().split()))
b_arr = list(map(int,input().split()))
res = ''

for i in range(a - b + 1):
    if a_arr[i:i+b] == b_arr:
        res = 'Yes'
        break
    else :
        res = 'No'

print(res)   