a,b,c = map(int,input().split())
is_contains = False

for i in range(a,b+1):
    if i % c == 0:
        is_contains = True
    
if is_contains == True:
    print('NO')
else:
    print('YES')