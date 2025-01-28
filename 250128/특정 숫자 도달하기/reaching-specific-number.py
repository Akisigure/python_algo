arr = input().split()
n = len(arr)
avg = 0.0
s = 0
cnt = 0

for i in range(n):
    i_arr = int(arr[i])
    if i_arr >= 250:
        break
    else :
        s += i_arr
        cnt += 1

avg = s / cnt

print('%d %.1f' %(s,avg))
    