word1 = input()
word2 = input()

# Write your code here!

a = sorted(word1)
b = sorted(word2)

if a != b:
    print('No')
else:
    print('Yes')