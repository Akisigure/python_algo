n = int(input())

is_cn = False

for i in range(2,n):
    if n % i == 0:
        is_cn = True

if is_cn == True:
    print('C')
else:
    print('N')