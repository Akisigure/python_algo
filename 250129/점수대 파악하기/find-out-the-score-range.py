c_arr = [0] * 11

arr = list(map(int,input().split()))

for i in arr :
    c_arr[i // 10] += 1

    if i == 0:
         c_arr[i // 10] += 1
         break

for i in range(100,9,-10):
    print('%d - %d' %(i,c_arr[i // 10]))