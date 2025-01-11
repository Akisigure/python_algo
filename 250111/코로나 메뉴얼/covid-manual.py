a ,b = input().split()
c ,d = input().split()
e ,f = input().split()


b,d,f = int(b),int(d),int(f)

emergency = 0

if b >= 37 and a == 'Y' :
    emergency += 1

if d >= 37 and c == 'Y' :
    emergency += 1

if f >= 37 and e == 'Y' :
    emergency += 1

if emergency >= 2 :
    print('E')
else :
    print('N')

