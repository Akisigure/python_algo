arr = list(map(int,input().split()))

n = len(arr)
arr2 = []

for i in range(n):
    if arr[i] == 0:
        break
    else :
        arr2.append(arr[i])

res = [i + 3 if i % 2 == 1 else i // 2 for i in arr2]

for i in res :
    print(i,end=' ')