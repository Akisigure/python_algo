arr = list(map(int,input().split()))

n = len(arr)
for i in range(n,10):
    arr.append(arr[-1] + arr[-2])

res = [i % 10 for i in arr]

for i in res :
    print(i,end=' ')