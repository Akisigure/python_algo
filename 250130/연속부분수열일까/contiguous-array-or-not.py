a,b = map(int,input().split())

a_arr = list(map(int,input().split()))
b_arr = list(map(int,input().split()))

ln = 0

for i in range(b):
    for j in range(a):
        if a_arr[j] == b_arr[i] :
            ln += 1

if ln != b :
    print('Yes')
else :
    print('No')
    