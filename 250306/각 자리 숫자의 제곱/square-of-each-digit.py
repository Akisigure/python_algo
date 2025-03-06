N = int(input())

# Please write your code here.
def get_num_squre_plus(num):
    if num == 0:
        return num
    return (num % 10) ** 2 + get_num_squre_plus(num // 10)
    

res = get_num_squre_plus(N)
print(res)