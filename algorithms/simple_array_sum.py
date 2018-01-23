"""
    Given an array of N integers, can you find sum of its elements
    Input:
        The first line contains an integer, N , denoting the size of the array.
        The second line contains N space-separated integers representing the array's elements.
    Output:
        Print the sum of the array's elements as a single integer.
    strip(): return copy of string
    strip([char]): return copy of string and remove char in that string
"""


def simpleArraySum(n, ar):
    return sum(ar)


n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)


