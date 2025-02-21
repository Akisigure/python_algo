lst = list(map(str, input()))
stack = []
vali = ['(', ')']
# Write your code here!
res = 'Yes'
for i in range(len(lst)):

    stack.append(lst[i])
    if stack and stack[-1] == ')':
        stack.pop()
        stack.pop()

if stack:
    res = 'No'

print(res)
