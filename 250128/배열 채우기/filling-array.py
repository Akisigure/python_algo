arr = list(map(int,input().split()))
n = len(arr)
ar = []

for i in range(n) :
    if arr[i] == 0:
        break
    else :
        ar.append(arr[i])

for j in ar[::-1]:
    print(j,end=' ')