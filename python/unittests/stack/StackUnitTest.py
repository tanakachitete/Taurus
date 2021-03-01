"""
NAME: StackUnitTest
AUTHOR: Tanaka Chitete
PURPOSE: Implement a basic unit test for Stack
CREATION: 01/03/2021
LAST MODIFICATION: 01/03/2021
"""

from Stack import Stack

def main():
    try:
        # Instantiation
        stack = Stack()

        # Accessors and Mutators
        print("push Test (View code)")
        pushTest(stack, 100)
        print("Number of elements: {0}".format(len(stack)))
        print("peek Test\nElement 0: {0}".format(stack.peek()))
        print("pop Test\nTOP OF THE STACK")
        popTest(stack)
        print("BOTTOM OF THE STACK")
    except RuntimeError as e:
        print(e)
    except AttributeError as e:
        print(e)

def pushTest(stack, numPushElements):
    for i in range(numPushElements):
        stack.push(i)

def popTest(stack):
    for i in range(len(stack)):
        print("Element {0}: {1}".format(i, stack.pop()))

if __name__ == "__main__":
    main()