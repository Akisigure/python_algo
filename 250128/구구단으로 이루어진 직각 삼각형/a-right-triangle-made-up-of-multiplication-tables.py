n = int(input())
a = 0
for i in range(1,n+1):
    for j in range(1,(n + 1) - (i -1)):
        
        if  j <= n - i:
            print(f'{i} * {j} = {i * j}',end=' / ')
        else :
            print(f'{i} * {j} = {i * j}')
        
            
