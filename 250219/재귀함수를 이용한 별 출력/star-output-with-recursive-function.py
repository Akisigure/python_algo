n = int(input())

# Write your code here!

def print_star(num):

    if num == 0:
        return
    print_star(num - 1)
    print('*' * num)
    


print_star(n)