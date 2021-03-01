"""
NAME: Node
AUTHOR: Tanaka Chitete
PURPOSE: Implement a node for a Linked List
CREATION: 27/02/2021 
LAST MODIFICATION: 27/02/2021
"""

class Node:

    """
    ALTERNATE CONSTRUCTOR
    IMPORT(S): element
    EXPORT(S): Address of new Node
    PURPOSE: Make new Node in alternate state
    CREATION: 27/02/2021
    LAST MODIFICATION: 27/02/2021
    """

    def __init__(self, element):
        self.element = element
        self.previous = None
        self.next = None