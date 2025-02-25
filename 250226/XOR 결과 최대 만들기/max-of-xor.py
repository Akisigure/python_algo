from itertools import combinations
from functools import reduce

n, m = map(int, input().split())
A = list(map(int, input().split()))

lst = list(combinations(A, m))
mv = -1 

for i in lst:
    xor_value = reduce(lambda x, y: x ^ y, i) 
    mv = max(mv, xor_value)

print(mv)
