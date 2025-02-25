from itertools import combinations

n, m = map(int, input().split())
A = list(map(int, input().split()))

lst = list(combinations(A,m))
mv = -1
# Write your code here!

for i in lst:
    xor_value = i[0]
    for num in i[1:]:
        xor_value ^= num
    mv = max(mv,xor_value)

print(mv)
