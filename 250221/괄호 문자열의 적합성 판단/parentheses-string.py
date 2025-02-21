lst = list(map(str, input()))
stack = []
dic = {')': '('}
# Write your code here!
res = 'Yes'
for i in range(len(lst)):
    stack.append(lst[i])
    if stack[-1] != lst[i]:
        stack.pop()

if stack:
    res = 'No'

print(res)

