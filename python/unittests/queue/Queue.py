"""
NAME: Queue
AUTHOR: Tanaka Chitete
PURPOSE: Implement a Queue
CREATION: 01/03/2021
LAST MODIFICATION: 01/03/2021
"""

from LinkedList import LinkedList

class Queue:
    # CONSTRUCTORS

    """
    DEFAULT CONSTRUCTOR
    IMPORT(S): NONE
    EXPORT(S): Address of new Queue
    PURPOSE: Make new Queue in default state
    CREATION: 01/03/2021
    LAST MODIFICATION: 01/03/2021
    """

    def __init__(self):
        self.__queue = LinkedList()


    # SETTERS (MUTATORS)

    def enqueue(self, element):
        successful = False
        if element != None:
            self.__queue.insertLast(element)
            successful = True
        return successful
        
    # GETTERS (ACCESSORS)

    def peek(self):
        if self.isEmpty():
            raise RuntimeError("Cannot peek at an element from an empty stack")
        else:
            return self.__queue.peekFirst()


    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Cannot pop an element from an empty stack")
        else:
            return self.__queue.removeFirst()


    # OPERATORS

    def isEmpty(self):
        return self.__queue.isEmpty()

    
    def __len__(self):
        return len(self.__queue)