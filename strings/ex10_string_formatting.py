def print_formatted(number):
    return '{} {} {} {}'.format(number, oct(number)[1:], hex(number)[2:], bin(number)[2:])


n = input()
for i in range(1, n+1):
    print(print_formatted(i))