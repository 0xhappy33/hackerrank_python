import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


# For example to test wrap function
s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
print(wrap(s, 4))
