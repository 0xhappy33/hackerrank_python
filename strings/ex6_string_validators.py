if __name__ == '__main__':
    s = input()
    # for method in [s.isalnum(), s.isalpha(), s.isdigit(), s.islower(), s.isupper()] :
    #     print(any(method(c) for c in s))

    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for c in s))
