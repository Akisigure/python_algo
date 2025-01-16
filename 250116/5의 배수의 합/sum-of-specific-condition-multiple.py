a,b = map(int,input().split())
t = 0

if a > b :
    for i in range(b,a+1):
        if i % 5 == 0:
            t += i
elif a < b:
    for i in range(a,b+1):
        if i % 5 == 0:
            t += i
else :
    for i in range(1,a+1):
        if i % 5 == 0:
            t += i    


print(t)
