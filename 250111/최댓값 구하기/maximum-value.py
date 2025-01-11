a,b,c = input().split()

a,b,c = int(a),int(b),int(c)

maxi = -9999

# or 비교일경우 가장 앞에서 True가 되면 통과해버림.

if a > b :
    maxi = a
elif a > c:
    maxi = a

if b > a :
    maxi = b
elif b > c :
    maxi = c

if c > a:
    maxi = c
elif c > b:
    maxi = c

print(maxi)
