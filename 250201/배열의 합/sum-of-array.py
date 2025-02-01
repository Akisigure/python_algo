n = 4 

arr = [list(map(int,input().split())) for _ in range(n)]


for i in range(n):
    s = 0
    for j in range(n): 
        s += arr[i][j]
    print(s)