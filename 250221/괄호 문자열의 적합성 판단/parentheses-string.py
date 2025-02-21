
lst = list(map(str,input()))
stack = []
stack_2 = []
# Write your code here!
res = 'Yes'
for i in range(len(lst)):
    if lst[i] == '(':
        stack.append(lst[i])
    if lst[i] == ')':
        stack_2.append(lst[i])

if len(stack) != len(stack_2):
    res = 'No'
print(res)