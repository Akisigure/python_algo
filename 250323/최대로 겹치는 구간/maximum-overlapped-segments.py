n = int(input())
arr = [0] * 201
mv = -99999

for i in range(n):
    a,b = map(int,input().split())
    a += 101
    b += 101
    for j in range(a,b):
        arr[j] += 1
        mv = max(mv,arr[j])

print(mv)
