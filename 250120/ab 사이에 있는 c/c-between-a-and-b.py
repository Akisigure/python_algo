a,b,c = map(int,input().split())

isContains = False

for i in range(a,b+1):
    if i % c == 0:
        isContains = True

if isContains == True :
    print('YES')
else :
    print('NO')