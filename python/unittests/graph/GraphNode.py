"""
NAME: GraphNode
AUTHOR: Tanaka Chitete
PURPOSE: Implement a node for a Linked List
CREATION: 01/03/2021 
LAST MODIFICATION: 01/03/2021
"""

from LinkedList import LinkedList

class GraphNode:
    # CONSTRUCTORS

    """
    ALTERNATE CONSTRUCTOR
    IMPORT(S): element
    EXPORT(S): Address of new GraphNode
    PURPOSE: Make new GraphNode in alternate state
    CREATION: 01/03/2021
    LAST MODIFICATION: 01/03/2021
    """

    def __init__(self, label):
        if label == None:
            raise ValueError("Cannot instantiate a GraphNode with a None label")
        else:
            self.label = label
            self.neighbours = LinkedList()
            self.wasVisitedBool = False


    # SETTERS (MUTATORS)

    def addNeighbour(self, neighbour):
        self.neighbours.insertLast(neighbour)

    
    def wasVisited(self):
        return self.wasVisitedBool