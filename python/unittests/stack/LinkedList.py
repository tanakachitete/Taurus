"""
NAME: LinkedList
AUTHOR: Tanaka Chitete
PURPOSE: Implement a Linked List
CREATION: 27/02/2021
LAST MODIFICATION: 01/03/2021
"""

from LinkedListNode import LinkedListNode

class LinkedList:
    # CONSTRUCTORS

    """
    DEFAULT CONSTRUCTOR
    IMPORT(S): NONE
    EXPORT(S): Address of new LinkedList
    PURPOSE: Make new LinkedList in default state
    CREATION: 28/02/2021
    LAST MODIFICATION: 28/02/2021
    """

    def __init__(self):
        self.__first = None
        self.__last = None
        self.__count = 0


    # SETTERS (MUTATORS)

    def insertFirst(self, newFirstElement):
        newFirst = LinkedListNode(newFirstElement)

        if self.isEmpty():
            self.__first = newFirst
            self.__last = newFirst
        else:
            newFirst.next = self.__first
            self.__first = newFirst
        self.__count += 1


    def insertLast(self, newLastElement):
        newLast = LinkedListNode(newLastElement)

        if self.isEmpty():
            self.__last = newLast
            self.__first = newLast
        else:
            self.__last.next = newLast
            self.__last = newLast
        self.__count += 1


    # GETTERS (ACCESSORS)

    def peekFirst(self):
        if self.isEmpty():
            raise ValueError("Cannot peek at the first node of an empty linked list")
        else:
            return self.__first.element


    def peekLast(self):
        if self.isEmpty():
            raise ValueError("Cannot peek at the last node of an empty linked list")
        else:
            return self.__last.element


    def removeFirst(self):
        if self.isEmpty():
            raise ValueError("Cannot remove the first node of an empty linked list")
        else:
            removedFirstElement = self.__first.element
            self.__first = self.__first.next
            self.__count -= 1
            return removedFirstElement


    def removeLast(self):
        if self.isEmpty():
            raise ValueError("Cannot remove the last node of an empty linked list")
        elif self.__first.next == None:
            removedLastElement = self.__first.element
            self.__first = None
            self.__count -= 1
            return removedLastElement
        else:
            removedLastElement = self.__last.element
            self.__last = self.__last.previous
            self.__last.next = None
            self.__count -= 1
            return removedLastElement


    # OPERATORS

    def isEmpty(self):
        return self.__first is None


    def __len__(self):
        return self.__count


    # ITERATOR

    def __iter__(self):
        return Iterator(self)
    

    class Iterator:
        def __init__(self, inLinkedList):
            self.next = inLinkedList.__first

        def __next__(self):
            element = None
            if self.next is not None:
                element = self.next.element
                self.next = self.next.next
            return element