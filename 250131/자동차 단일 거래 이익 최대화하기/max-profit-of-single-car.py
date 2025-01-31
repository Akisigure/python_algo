
import sys

n = int(input())
price = list(map(int, input().split()))

min_price = sys.maxsize
max_price = -sys.maxsize
min_idx = 0
calc = 0
# Write your code here!

for i in range(n):
    if price[i] < min_price :
        min_price = price[i]
        min_idx = i

for i in price[min_idx:] :
    if i > max_price :
        max_price = i

if max_price < min_price :
    calc = 0

calc = max_price - min_price

print(calc)