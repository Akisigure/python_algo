lst = list(map(str, input()))
stack = []
vali = ['(', ')']
# Write your code here!
res = 'Yes'
for i in range(len(lst)):

    for ch in lst:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                res = 'No'
                break

if stack:
    res = 'No'

print(res)

