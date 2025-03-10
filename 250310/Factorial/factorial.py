N = int(input())

# Please write your code here.

def factorial(num):
    if num == 0:
        return 1
    return factorial(num - 1) * num

print(factorial(N))