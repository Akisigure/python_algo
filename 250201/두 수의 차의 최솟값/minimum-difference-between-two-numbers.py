import sys

n = int(input())
arr = list(map(int,input().split()))
a = 0
calc = sys.maxsize

for i in range(n):
    for j in range(i+1,n):
        a = arr[j] - arr[i]
        if calc > a :
            calc = a

print(calc)