n = int(input())

for i in range(1,n+1):
    is_prime = 0
    for j in range(1,i+1):
        if i != 1 and i % j == 0:
            is_prime += 1
    if is_prime == 2:
        print(i,end=' ')
