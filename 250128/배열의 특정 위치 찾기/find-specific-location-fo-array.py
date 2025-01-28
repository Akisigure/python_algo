arr = list(map(int,input().split()))

n = len(arr)

even_summary = 0

odd_summary = 0
odd_cnt = 0

for i in range(n):
    
    if arr[i] % 2 == 0:
        even_summary += arr[i]
    if arr[i] % 3 == 0:
        odd_summary += arr[i]
        odd_cnt += 1

odd_avg = odd_summary / odd_cnt 
print('%d %.1f' %(even_summary,odd_avg))
