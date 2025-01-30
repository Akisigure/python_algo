n = int(input())
nums = list(map(int, input().split()))

max_val = -1
# Write your code here!


for i in range(n):
    if nums.count(nums[i]) > 1:
        continue
    if nums[i] > max_val :
        max_val = nums[i]

print(max_val)


    