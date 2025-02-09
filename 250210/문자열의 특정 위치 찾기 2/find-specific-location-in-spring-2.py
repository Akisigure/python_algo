arr = ['apple', 'banana', 'grape', 'blueberry', 'orange']

n = input()
cnt = 0
for i in range(len(arr)):
    if n in arr[i][2] or n in arr[i][3]:
        cnt += 1
        print(arr[i])
        
print(cnt)