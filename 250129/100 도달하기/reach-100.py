n = int(input())
res = [1,n]

for i in range(2,100):
    res.append(res[-1] + res[-2])

    if res[i] >= 100:
        break

print(*res)