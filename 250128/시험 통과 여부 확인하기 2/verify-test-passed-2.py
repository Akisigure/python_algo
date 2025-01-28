n = int(input())
cnt = 0
avg = 0

for i in range(n):

    arr = list(map(int, input().split()))

    avg = sum(arr) / 4
    if avg >= 60.0 :
        avg = 0.0
        cnt += 1
        print('pass')
    else :
        avg = 0.0
        print('fail')
        

print(cnt)