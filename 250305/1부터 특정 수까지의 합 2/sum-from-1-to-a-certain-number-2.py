N = int(input())

# Please write your code here.

def rec_sum(num):
    if num == 1:
        return 1
    return rec_sum(num - 1) + num

res = rec_sum(N)
print(res)