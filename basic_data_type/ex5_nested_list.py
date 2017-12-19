if __name__ == '__main__':
    maths = []  # maths is called nested list
    for _ in range(int(input())):
        n = input()
        score = float(input())
        maths.append([n, score])

    # sort follow name
    second = sorted(list(set([marks for name, marks in maths])))
    # print(maths)
    print(maths[0][0] + '\n' + maths[1][0])