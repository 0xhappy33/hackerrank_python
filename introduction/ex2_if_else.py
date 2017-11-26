if __name__ == '__main__':
    n = int(input())
    if n % 2 != 0:
        print("Weird")
    elif n in range(2, 5) or n > 20:
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
