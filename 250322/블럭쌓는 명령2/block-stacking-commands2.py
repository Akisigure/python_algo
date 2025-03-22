n,k = map(int,input().split())

arr = [0] * (n + 1)
mv = -9999999
for i in range(k):
    a,b = map(int,input().split())
    for j in range(a,b + 1):
        arr[j] += 1
        mv = max(mv,arr[j])
print(mv)

