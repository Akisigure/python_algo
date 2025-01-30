n = int(input())
nums = list(map(int, input().split()))

max_val = -1
# Write your code here!

for i in range(n):
    if max_val == nums[i]:
        max_val = -1

    if nums[i] > i :
        max_val = nums[i]



print(max_val)    
    