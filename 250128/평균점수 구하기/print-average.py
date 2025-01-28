arr = list(map(float,input().split()))

s = sum(arr)

cnt = len(arr)

avg = s / cnt

print('%.1f' %avg)