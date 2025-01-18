avg = 0.0
cnt = 0
while True:
    a = int(input())
    if a >= 30:
        break
    elif 10 >= a:
        break
    
    avg += a
    cnt += 1
print('%.2f' %(avg / cnt))