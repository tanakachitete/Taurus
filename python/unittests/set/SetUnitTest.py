"""
NAME: SetUnitTest
AUTHOR: Tanaka Chitete
PURPOSE: Implement a basic unit test for Set
CREATION: 02/03/2021 
LAST MODIFICATION: 02/03/2021
"""

from Set import Set
from UserInterface import getInt, getStr

def main():
    QUIT = 0
    OPTION_1 = 1
    OPTION_2 = 2
    OPTION_3 = 3
    OPTION_4 = 4
    OPTION_6 = 6

    mySet = Set()
    while True:
        print("Main Menu\n\n" + \
            "1. Add\n" + \
            "2. Remove\n" + \
            "3. Has\n" + \
            "4. Print\n" + \
            "0. Quit\n"
        )
        prompt = "Input: "
        userInput = getInt(QUIT, OPTION_4, prompt)

        if userInput == OPTION_1:
            add(mySet)
        elif userInput == OPTION_2:
            remove(mySet)
        elif userInput == OPTION_3:
            has(mySet)
        elif userInput == OPTION_4:
            display(mySet)

        if userInput == QUIT:
            break


def add(mySet):
    print("\nAdd\n")

    prompt = "Element: "
    element = getStr(prompt)
    mySet.add(element)
    print()


def remove(mySet):
    print("\nRemove\n")

    prompt = "Element: "
    element = getStr(prompt)
    mySet.remove(element)
    print()


def has(mySet):
    print("\nHas\n")

    prompt = "Element: "
    element = getStr(prompt)
    print()

    if mySet.has(element):
        print("Element is present in Set")
    else:
        print("Element is not present in Set")


def display(mySet):
    print("\nPrint\n")

    print(mySet)
    print()

if __name__ == "__main__":
    main()