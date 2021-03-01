// Obtained from Tanaka Chitete
// (accessed 15/10/2020)

import java.util.*;

public class GraphTestHarness {
    public static void main(String[] args) {
        try {
            Graph undirectedGraph = new Graph();
            Graph directedGraph = new Graph(true);

            System.out.println("UNDIRECTED GRAPH\n");
            testAddVertex(undirectedGraph);
            testAddEdge(undirectedGraph);
            testDisplayList(undirectedGraph);
            testDisplayMatrix(undirectedGraph);
            testHasNode(undirectedGraph);
            testAreNeighbours(undirectedGraph);
            testNodeCount(undirectedGraph);
            testEdgeCount(undirectedGraph);
            testBfs(undirectedGraph);
            testDfs(undirectedGraph);

            System.out.println("DIRECTED GRAPH\n");
            testAddVertex(directedGraph);
            testAddEdge(directedGraph);
            testDisplayList(directedGraph);
            testDisplayMatrix(directedGraph);
            testHasNode(directedGraph);
            testAreNeighbours(directedGraph);
            testNodeCount(directedGraph);
            testEdgeCount(directedGraph);
            testBfs(directedGraph);
            testDfs(directedGraph);
        }
        catch (NoSuchElementException e) {
            System.out.println(e.getMessage());
        }
    }

    private static void testAddVertex(Graph graph) {
        graph.add("A");
        graph.add("B");
        graph.add("C");
        graph.add("D");
        graph.add("E");
        graph.add("F");
        graph.add("G");
        graph.add("S");
    }

    private static void testAddEdge(Graph graph) {
        graph.connect("A", "B");
        graph.connect("A", "S");
        graph.connect("C", "D");
        graph.connect("C", "E");
        graph.connect("C", "F");
        graph.connect("C", "S");
        graph.connect("F", "G");
        graph.connect("S", "G");
    }

    private static void testDisplayList(Graph graph) {
        System.out.println("displayList");
        graph.displayList();
        System.out.println();
    }

    private static void testDisplayMatrix(Graph graph) {
        System.out.println("displayMatrix");
        graph.displayMatrix();
        System.out.println();
    }

    private static void testHasNode(Graph graph) {
        System.out.println("hasNode");
        System.out.println("D: " + graph.hasNode("D"));
        System.out.println("F: " + graph.hasNode("F"));
        System.out.println("K: " + graph.hasNode("K") + "\n");
    }

    private static void testAreNeighbours(Graph graph) {
        System.out.println("areNeighbours");
        System.out.println("D,F: " + graph.areNeighbours("D", "F"));
        System.out.println("F,G: " + graph.areNeighbours("F", "G"));
        System.out.println("B,C: " + graph.areNeighbours("B", "C") + "\n");
    }

    private static void testNodeCount(Graph graph) {
        System.out.println("nodeCount");
        System.out.println(graph.nodeCount() + "\n");
    }

    private static void testEdgeCount(Graph graph) {
        System.out.println("edgeCount");
        System.out.println(graph.edgeCount() + "\n");
    }

    private static void testBfs(Graph graph) {
        Queue<String> visited = graph.bfs();
        System.out.println("bfs\n" + visited + "\n");
    }

    private static void testDfs(Graph graph) {
        Queue<String> visited = graph.dfs();
        System.out.println("dfs\n" + visited + "\n");
    }
}