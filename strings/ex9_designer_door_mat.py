n, m = map(int, raw_input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
