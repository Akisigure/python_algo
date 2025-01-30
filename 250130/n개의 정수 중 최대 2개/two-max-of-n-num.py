n = int(input())
a = list(map(int, input().split()))

# Write your code here!

a.sort()
a = [i for i in a[::-1]]

for i in range(2):
    print(a[i],end=' ')