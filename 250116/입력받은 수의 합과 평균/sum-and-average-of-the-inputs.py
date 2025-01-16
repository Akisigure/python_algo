cnt = int(input())
sum_value = 0
avg = 0.0

for i in range(cnt):
    a = int(input())
    sum_value += a

avg = sum_value / cnt

print('%d %.1f' %(sum_value,avg),end=' ')