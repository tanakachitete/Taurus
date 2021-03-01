"""
NAME: Stack
AUTHOR: Tanaka Chitete
PURPOSE: Implement a Stack
CREATION: 01/03/2021
LAST MODIFICATION: 01/03/2021
"""

from LinkedList import LinkedList

class Stack:
    # CONSTRUCTORS

    """
    DEFAULT CONSTRUCTOR
    IMPORT(S): NONE
    EXPORT(S): Address of new Stack
    PURPOSE: Make new Stack in default state
    CREATION: 01/03/2021
    LAST MODIFICATION: 01/03/2021
    """

    def __init__(self):
        self.__stack = LinkedList()


    # SETTERS (MUTATORS)

    def push(self, element):
        successful = False
        if element != None:
            self.__stack.insertFirst(element)
            successful = True
        return successful
        
    # GETTERS (ACCESSORS)

    def peek(self):
        if self.isEmpty():
            raise RuntimeError("Cannot peek at an element from an empty stack")
        else:
            return self.__stack.peekFirst()


    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Cannot pop an element from an empty stack")
        else:
            return self.__stack.removeFirst()


    # OPERATORS

    def isEmpty(self):
        return self.__stack.isEmpty()

    
    def __len__(self):
        return len(self.__stack)