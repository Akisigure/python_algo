n = int(input())
price = list(map(int, input().split()))
calc = 0

for i in range(n - 1):
    for j in range(i, n):
        if price[i] < price[j] and price[j] - price[i] > calc:
            calc = price[j] - price[i]

print(calc)
