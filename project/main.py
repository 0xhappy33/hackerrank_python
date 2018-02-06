import re


print("Our Magical Calculator")
print("Type 'quit' to exit \n")

previous = 0
run = True


def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("Good bye guys!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        # Here if "you typed" + previous => previous is string
        # if "you typed", previous => previous is int
        print("You typed ", previous)


while run:
    performMath()
