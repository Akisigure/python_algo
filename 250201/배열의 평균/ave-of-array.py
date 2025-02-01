n = 2 
m = 4

arr = [list(map(int,input().split())) for _ in range(n)]

p = 0
avg = []
i_avg = []
t_avg = 0.0

for i in range(n):
    t = 0
    for j in range(m):
        t += arr[i][j]
        t_avg += arr[i][j]
    avg.append(t)
    avg[i] = avg[i] / m

for i in range(m):
    p = arr[0][i] + arr[1][i]
    i_avg.append(p)

    i_avg[i] = i_avg[i] / 2 

t_avg = t_avg / (n * m)

for i in avg :
    print(f'{i:.1f}',end=' ')
print()
for i in i_avg :
    print(f'{i:.1f}',end=' ')
print()
print(f'{t_avg:.1f}')