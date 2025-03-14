n = int(input())

# Please write your code here.
cnt = 0
def f(num):

    global cnt

    if num == 1:
        return
    cnt += 1
    if num % 2 == 0:
        return f(num // 2)
    if num % 2 != 0:
        return f(num * 3 + 1)

    

f(n)

print(cnt)