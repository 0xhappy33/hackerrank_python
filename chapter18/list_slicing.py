# 0 1 2 3 4 5 6 7
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

if __name__ == '__main__':
    print(lst[::2])
    # Output: ['a', 'c', 'e', 'g']
    print(lst[2:4])
    # Output: ['c', 'd']
    print(lst[2:])
    # Output: ['c', 'd', 'e', 'f', 'g', 'h']
