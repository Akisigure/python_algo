a,b = input().split()

a_len = len(a)
b_len = len(b)

if a_len > b_len :
    print(a,a_len)
if b_len > a_len :
    print(b,b_len)
if a_len == b_len:
    print('same')