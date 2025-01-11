a = int(input())

# 1 31 2 28 3 31 4 30 5 31 6 30 7 31 8 31 9 30 10 31 11 30 12 31
# 1 3 5 7 8 10 12

if a == 1 or a == 3 or a == 5 or a== 7 or a == 8 or a == 10 or a == 12 :
    print('31')
elif a == 2 :
    print('28')
else :
    print('30')
    