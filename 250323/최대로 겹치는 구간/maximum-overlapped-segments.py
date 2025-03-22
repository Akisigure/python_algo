n = int(input())
arr = [0] * 101
mv = -99999

for i in range(n):
    a,b = map(int,input().split())
    for j in range(a,b):
        arr[j] += 1
        mv = max(mv,arr[j])


print(mv)