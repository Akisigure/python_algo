n = int(input())

# Write your code here!
def num(integer):
    for i in range(1,integer + 1):
        print(i,end=' ')
    print()
    for i in range(integer,0,-1):
        print(i,end=' ')

num(n)