# Other smaller codes may also exist,
# but using list comprehensions is always a good option.
# Code using list comprehensions:
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print ([[i, j, k]
            for i in range(x + 1)
            for j in range(y + 1)
            for k in range(z + 1)
            if (i + j + k) != n])
