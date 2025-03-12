a, b, c = map(int, input().split())

# Please write your code here.

res = a * b * c
res = str(res)


def r_f(res,s,cnt):
    if cnt == len(res) - 1:
        return s + int(res[cnt])

    return r_f(res,s + int(res[cnt]),cnt + 1)


r = r_f(res,0,0)
print(r)