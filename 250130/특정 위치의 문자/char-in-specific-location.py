w = input()
arr = ['L','E','B','R','O','S']

a = -1
t = 'None'

for i, char in enumerate(arr) :
    if char == w:
        a = i
        
if a > -1 :
    print(a)
else :
    print(t)