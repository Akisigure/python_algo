N = int(input())

# Please write your code here.

cnt = 0

def div_num(num):
    global cnt

    if num == 1:
        return
    elif num % 2 == 0:
        cnt += 1
        return div_num(num // 2)
        
    elif num % 2 != 0:
        cnt += 1
        return div_num(num // 3)

div_num(N)

print(cnt)
        