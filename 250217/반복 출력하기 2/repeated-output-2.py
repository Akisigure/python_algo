n = int(input())

def print_word(arg):
    if arg == 0:
        return
    print_word(arg - 1)
    print('HelloWorld')

print_word(n)