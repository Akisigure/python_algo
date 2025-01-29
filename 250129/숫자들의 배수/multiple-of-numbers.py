n = int(input())

cnt = 0

arr = [i * n for i in range(1,100)]

for i in arr :
    if i % 5 == 0 :
        cnt += 1
    if cnt == 2:
        print(i,end=' ')
        break
    else :
        print(i, end=' ')