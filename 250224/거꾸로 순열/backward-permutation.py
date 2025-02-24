from itertools import permutations
n = int(input())

# Write your code here!
arr = [i for i in range(1,n + 1)]
p_arr = list(permutations(arr))

for i in range(len(p_arr)-1,-1,-1):
    a,b,c = p_arr[i]
    print(a,b,c)