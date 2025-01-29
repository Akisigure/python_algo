c_arr = [0] * 10
arr = list(map(int,input().split()))

for i in arr :
    if i == 0:
        c_arr[i // 10] += 1
        break
    else :
        c_arr[i // 10] += 1

c_len = len(c_arr)

for i in range(1,c_len):
    print('%d - %d' %(i,c_arr[i]))