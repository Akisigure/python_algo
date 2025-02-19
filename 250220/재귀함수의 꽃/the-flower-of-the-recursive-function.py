n = int(input())

def minus_plus(num):
    if num == 0:
        return
    print(num,end=' ')
    minus_plus(num - 1)
    print(num,end=' ')

minus_plus(n)        