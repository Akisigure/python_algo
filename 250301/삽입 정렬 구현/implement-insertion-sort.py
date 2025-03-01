n = int(input())
grid = list(map(int,input().split()))

# Please write your code here.
grid.sort()
print(*grid)