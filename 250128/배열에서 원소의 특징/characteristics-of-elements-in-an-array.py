arr = list(map(int,input().split()))

a = 0

for i in arr :
    if i % 3 == 0:
        break
    else :
        a = i

print(a)
    