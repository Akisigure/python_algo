arr = list(map(int,input().split()))

n = len(arr)
odd_sum = 0
even_sum = 0
total = 0

for i in range(n) :
    if (i + 1) % 2 == 0:
        even_sum += arr[i]
    else :
        odd_sum += arr[i]

    if even_sum > odd_sum :
        total = even_sum - odd_sum
    elif odd_sum > even_sum :
        total = odd_sum - even_sum
    else :
        total = even_sum - odd_sum

print(total)
