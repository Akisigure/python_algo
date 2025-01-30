arr = list(map(int,input().split()))
mv = 0

for i in arr :
    if i > mv :
        mv = i

print(mv)