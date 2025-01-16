sum_value = 0
cnt = 0
avg = 0.0
for i in range(1,11):
    n = int(input())
    if n >= 0 and n <= 200:
        sum_value += n
        cnt += 1

avg = sum_value / cnt
print('%s %.1f' %(sum_value,avg), end=' ')
