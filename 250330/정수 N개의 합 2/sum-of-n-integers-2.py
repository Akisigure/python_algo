n, k = map(int, input().split())
arr = list(map(int, input().split()))
s = [0] * (n + 1)

for i in range(n):
    s[i + 1] = s[i] + arr[i]

max_sum = -999999999

for i in range(n - k + 1):
    max_sum = max(max_sum,s[i + k] - s[i])
print(max_sum)