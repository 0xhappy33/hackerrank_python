def split_and_join(line):
    return "-".join(line.split(" "))


if __name__ == '__main__':
    print(split_and_join("this is a string"))