n = int(input())

# Please write your code here.
arr = [0] * 101
for i in range(n):
    x,y = map(int,input().split())
    for j in range(x,y + 1):
        arr[j] += 1

mv = -1
for i in range(len(arr)):
    mv = max(mv,arr[i])

print(mv)

