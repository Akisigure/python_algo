n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(n):
    for j in range(i,n-1):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

print(*arr)