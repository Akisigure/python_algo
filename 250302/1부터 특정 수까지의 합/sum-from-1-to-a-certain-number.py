n = int(input())


# Please write your code here.

def num_sum(n):
    val = 0
    for i in range(1,n + 1):
        val += i
    val /= 10
    return val


print(int(num_sum(n)))
