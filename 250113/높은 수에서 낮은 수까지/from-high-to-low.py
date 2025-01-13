a,b = map(int,input().split())

a,b = int(a),int(b)

if b > a :
    for i in range(b,a-1,-1):
        print(i, end=' ')
else :
    for i in range(a,b-1,-1):
        print(i, end=' ')