"""
NAME: LinkedListNode
AUTHOR: Tanaka Chitete
PURPOSE: Implement a node for a Linked List
CREATION: 27/02/2021 
LAST MODIFICATION: 1/03/2021
"""

class LinkedListNode:
    # CONSTRUCTORS

    """
    ALTERNATE CONSTRUCTOR
    IMPORT(S): element
    EXPORT(S): Address of new LinkedListNode
    PURPOSE: Make new LinkedListNode in alternate state
    CREATION: 27/02/2021
    LAST MODIFICATION: 27/02/2021
    """

    def __init__(self, element):
        self.element = element
        self.previous = None
        self.next = None