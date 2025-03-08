N = int(input())

# Please write your code here.

cnt = 0
res = 0
def fibo(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    
    return fibo(num - 1) + fibo(num - 2)

r = fibo(N)
print(r)
