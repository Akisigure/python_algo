a,b = input().split()
a,b = int(a),int(b)

for i in range(a,b+1,a + 1):
    print(i, end=' ')