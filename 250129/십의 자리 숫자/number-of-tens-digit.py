c_arr = [0] * 10
arr = list(map(int,input().split()))

for i in arr :
    c_arr[i // 10] += 1

c_len = len(c_arr)

for i in range(1,c_len):
    print('%d - %d' %(i,c_arr[i]))