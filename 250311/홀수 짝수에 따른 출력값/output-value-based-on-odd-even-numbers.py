n = int(input())


def odd_or_even(num):

    if num % 2 != 0:
        if num == 1:
            return 1
        return odd_or_even(num - 2) + num

    else:
        if num == 2:
            return 2
        return odd_or_even(num - 2) + num


res = odd_or_even(n)
print(res)
