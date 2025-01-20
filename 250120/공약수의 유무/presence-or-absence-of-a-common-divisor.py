a,b = map(int,input().split())

is_divisor = False

for i in range(a,b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        is_divisor = True

if is_divisor == True:
    print(1)
else:
    print(0)