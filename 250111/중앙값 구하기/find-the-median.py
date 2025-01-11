a,b,c = input().split()

a,b,c = int(a),int(b),int(c)

mid = 0

if a > b and a < c:
    mid = a
elif b > a and b < c:
    mid = b
elif c > a and c < b :
    mid = c
elif a < b and a > c :
    mid = a
elif b < a and b > c :
    mid = b
elif c < a and c > b :
    mid = c

print(mid)