arr = list(map(int,input().split()))

n = len(arr)

even_summary = 0

odd_summary = 0
odd_cnt = 0

for i in range(n):
    
    if i % 2 != 0:
        even_summary += arr[i]
    if i == 2 or i == 5 or i == 8:
        odd_summary += arr[i]
        odd_cnt += 1

odd_avg = odd_summary / odd_cnt 
print('%d %.1f' %(even_summary,odd_avg))
