c_arr = [0] * 5

for i in range(3):
    arr = input().split()
    arr[1] = int(arr[1])

    if arr[0] == 'Y' and arr[1] >= 37 :
        c_arr[1] += 1
    elif arr[0] == 'N' and arr[1] >= 37 :
        c_arr[2] += 1
    elif arr[0] == 'Y' :
        c_arr[3] += 1
    else :
        c_arr[4] += 1

if c_arr[1] >= 2:
    c_arr.append('E')

c_len = len(c_arr)

for i in range(1,c_len):
    print(c_arr[i],end=' ')