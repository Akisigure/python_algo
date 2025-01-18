avg = 0.0
cnt = 0
while True:
    a = int(input())
    if a >= 30:
        break
    
    avg += a
    cnt += 1
print('%.2f' %(avg / cnt))