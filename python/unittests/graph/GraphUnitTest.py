"""
NAME: GraphUnitTest
AUTHOR: Tanaka Chitete
PURPOSE: Implement a basic unit test for Graph
CREATION: 01/03/2021 
LAST MODIFICATION: 01/03/2021
"""

from Graph import Graph

def main():
    undirectedGraph = Graph()
    directedGraph = Graph(True)

    try:
        print("UNDIRECTED GRAPH\n")
        testAdd(undirectedGraph)
        testConnect(undirectedGraph)
        testHas(undirectedGraph)
        testAreNeighbours(undirectedGraph)
        testNodeCount(undirectedGraph)
        testConnectionCount(undirectedGraph)
        testBfs(undirectedGraph)
        testDfs(undirectedGraph)
        testPrintPaths(undirectedGraph)

        print("DIRECTED GRAPH\n")
        testAdd(directedGraph)
        testConnect(directedGraph)
        testHas(directedGraph)
        testAreNeighbours(directedGraph)
        testNodeCount(directedGraph)
        testConnectionCount(directedGraph)
        testBfs(directedGraph)
        testDfs(directedGraph)
        testPrintPaths(directedGraph)
    except RuntimeError as e:
        print(e)
    except ValueError as e:
        print(e)


def testAdd(graph):
    graph.add("a")
    graph.add("b")
    graph.add("c")
    graph.add("d")
    graph.add("e")
    graph.add("f")
    graph.add("g")
    graph.add("s")


def testConnect(graph):
    graph.connect("a", "b")
    graph.connect("a", "s")
    graph.connect("c", "d")
    graph.connect("c", "e")
    graph.connect("c", "f")
    graph.connect("c", "s")
    graph.connect("f", "g")
    graph.connect("s", "g")


def testHas(graph):
    print("has")
    print("d: {0}".format(graph.has("d")))
    print("f: {0}".format(graph.has("f")))
    print("k: {0}\n".format(graph.has("k")))


def testAreNeighbours(graph):
    print("areNeighbours")
    print("d,f: {0}".format(graph.areNeighbours("d", "f")))
    print("f,g: {0}".format(graph.areNeighbours("f", "g")))
    print("b,c: {0}\n".format(graph.areNeighbours("b", "c")))


def testNodeCount(graph):
    print("nodeCount")
    print(graph.nodeCount())
    print()


def testConnectionCount(graph):
    print("connectionCount")
    print(graph.connectionCount())
    print()


def testBfs(graph):
    print("bfs")
    print(graph.bfs())
    print()


def testDfs(graph):
    print("dfs")
    print(graph.dfs())
    print()


def testPrintPaths(graph):
    print("getPaths")
    print("a,g:")
    graph.printPaths("a", "g")
    print()
    print("a,e:")
    graph.printPaths("a", "e")
    print()
    print("f,b:")
    graph.printPaths("f", "b")
    print()


if __name__ == "__main__":
    main()