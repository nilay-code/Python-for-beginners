import random
x= input("Please enter a number between 0 and 5\n")

x = int(x)


def win(x):
    y = random.randint(0,5)

    if x==y:
        print("You Won")
    else:
        print(y)
        print("Try Again")

win(x)