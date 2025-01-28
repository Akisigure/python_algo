n = int(input())

arr = list(map(float, input().split()))
    
s = sum(arr)

avg = s / n

print('%.1f' %(avg))

if avg >= 4.0 :
    print('Perfect')
elif avg >= 3.0 :
    print('Good') 
else :
    print('Poor')   