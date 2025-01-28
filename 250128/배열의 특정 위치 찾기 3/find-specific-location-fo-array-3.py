arr = list(map(int,input().split()))

arr2 = []
for i in arr :
    if i == 0:
        break
    else :
        arr2.append(i)

s = arr2[-1] + arr2[-2] + arr2[-3]

print(s)