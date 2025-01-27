n = int(input())
cnt = 0


for i in range(1,n+1):
    for j in range(1,n+1):
        cnt += 1
        if i % 2 != 0:
            print(cnt,end=' ')
        else :
            print(cnt + 1 + n - (j * 2),end=' ')
    print()