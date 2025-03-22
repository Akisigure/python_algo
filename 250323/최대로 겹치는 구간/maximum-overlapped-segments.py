n = int(input())
arr = [0] * 201
mv = -99999

for i in range(n):
    a,b = map(int,input().split())
    a += 100
    b += 100
    for j in range(a,b + 1):
        arr[j] += 1

for i in range(1, len(arr) - 1):
    if arr[i] == arr[i + 1]:
        if mv < arr[i]:
            mv = arr[i]

print(mv)