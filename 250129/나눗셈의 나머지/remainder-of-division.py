c_arr = [0] * 10
arr = list(map(int,input().split()))
mod = 0
for i in range(999):
    mod = arr[0] % arr[1]
    c_arr[mod] += 1
    arr[0] = arr[0] // arr[1]

    
    if arr[0] <= 1:
        break
    elif arr[0] < arr[1]:
        mod = arr[0] % arr[1]
        c_arr[mod] += 1
        break

c_len = len(c_arr)
s = 0

res = [i ** 2 for i in c_arr]    

for i in range(c_len):
    s += res[i]

print(s)

# 420 % 4 = 0
# 105 % 4 = 1
# 26 % 4 =  2
# 6 % 4 = 2

# 1 1 2