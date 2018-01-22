from itertools import ifilter

names = ['Fred', 'Wilma', 'Barney']


def long_name(name):
    return len(name) > 5


print (filter(long_name, names))
ifilter(long_name, names)
