a,b = map(int,input().split())

sum_value = 0

for i in range(a,b+1):
    if i % 6 == 0 and i % 8 != 0:
        sum_value += i

print(sum_value)