/*
 * NAME: Graph
 * CREATOR: Tanaka Chitete
 * STUDENT_ID: 20169321
 * UNIT: COMP1002
 * PURPOSE: Implement a general-purpose graph
 * CREATION: 19/09/2020
 * LAST MODIFICATION: 09/11/2020
 */

import java.io.Serializable;
import java.util.*;

public class Graph implements Serializable {
    // NESTED CLASSES

    private class Node implements Serializable {
        // PRIVATE CLASS FIELDS
    
        String label;
        LinkedList<Node> neighbours;
        boolean wasVisited;
    
        // CONSTRUCTORS
    
        /*
         * ALTERNATE CONSTRUCTOR
         * IMPORT(S): inLabel (String)
         * EXPORT(S): Address of new Node
         * PURPOSE: Create new Node in alternate state
         * CREATION: 25/09/2020
         * LAST MODIFICATION: 25/09/2020
         */
    
        public Node(String inLabel) {
            if (inLabel == null) {
                throw new IllegalArgumentException("Cannot initialise with a null label");
            }
            else {
                label = inLabel;
                neighbours = new LinkedList<Node>();
                wasVisited = false;
            }
        }
    
        // SETTERS (MUTATORS)
    
        private void addNeighbour(Node inNeighbour) {
            neighbours.insertLast(inNeighbour);
        }
    
        // OPERATORS
    
        private boolean wasVisited() {
            return wasVisited;
        }
    }

    // PRIVATE CLASS FIELDS

    private LinkedList<Node> nodes;
    private boolean isDirected;
    private int nodeCount;
    private int edgeCount;

    // CONSTRUCTORS

    /*
     * DEFAULT CONSTRUCTOR
     * IMPORT(S): NONE
     * EXPORT(S): Address of new Graph object
     * PURPOSE: Create new Graph in default state
     * CREATION: 23/09/2020
     * LAST MODIFICATION: 23/09/2020
     */

    public Graph() {
        nodes = new LinkedList<Node>();
        isDirected = false;
        nodeCount = 0;
        edgeCount = 0;
    }

    /*
     * ALTERNATE CONSTRUCTOR
     * IMPORT(S): isDirected
     * EXPORT(S): Address of new Graph object
     * PURPOSE: Create new Graph in alternate state
     * CREATION: 23/09/2020
     * LAST MODIFICATION: 23/09/2020
     */

    public Graph(boolean inDirected) {
        nodes = new LinkedList<Node>();
        isDirected = inDirected;
        nodeCount = 0;
        edgeCount = 0;
    }

    // SETTERS (MUTATORS)

    public void add(String inLabel) {
        if (inLabel == null) {
            throw new IllegalArgumentException("Cannot call add with a null label");
        }
        else if (hasNode(inLabel)) {
            throw new IllegalArgumentException("Cannot call add with a label that has " + 
                "already been assigned to a vertex");
        }
        else {
            Node vertex = new Node(inLabel);
            nodes.insertLast(vertex);
            nodeCount++;
        }
    }

    public void connect(String inSourceVertexLabel, String inSinkVertexLabel) {
        if (nodeCount < 2) {
            throw new IllegalArgumentException("Cannot call connect on a graph with less than " + 
                "two nodes");
        }
        else if (inSourceVertexLabel == null || inSinkVertexLabel == null) {
            throw new IllegalArgumentException("Cannot call connect with a null label");
        }
        else if (inSourceVertexLabel.equals(inSinkVertexLabel)) {
            throw new IllegalArgumentException("Cannot call connect with equivalent labels");
        }
        else {
            _connect(inSourceVertexLabel, inSinkVertexLabel);
            edgeCount++;
        }
    }

    // GETTERS (ACCESSORS)

    public Node get(String inLabel) {
        Node vertex;

        if (nodes.isEmpty()) {
            throw new IllegalArgumentException("Cannot call get on an empty graph");
        }
        else {
            vertex = _getVertex(inLabel);
        }

        return vertex;
    }

    public int nodeCount() {
        return nodeCount;
    }

    public int edgeCount() {
        return edgeCount;
    }

    // OPERATORS

    public boolean hasNode(String inLabel) {
        boolean hasNode;

        if (inLabel == null) {
            throw new IllegalArgumentException("Cannot call hasNode with a null label");
        }
        else {
            hasNode = _hasNode(inLabel);
        }

        return hasNode;
    }

    public boolean areNeighbours(String inSourceVertexLabel, 
        String inSinkVertexLabel) {
        boolean areNeighbours;
        if (nodeCount < 2) {
            throw new IllegalArgumentException("Cannot call areNeighbours on a graph with less " + 
                "than 2 nodes");
        }
        else if (inSourceVertexLabel == null || inSinkVertexLabel == null) {
            throw new IllegalArgumentException("Cannot call areNeighbours with a null label");
        }
        else if (inSourceVertexLabel.equals(inSinkVertexLabel)) {
            throw new IllegalArgumentException("Cannot call areNeighbours with equivalent labels");
        }
        else {
            areNeighbours = _areNeighbours(inSourceVertexLabel, inSinkVertexLabel);
        }

        return areNeighbours;
    }

    public Queue<String> bfs() {
        Queue<Node> next = new Queue<Node>();
        Queue<String> visited = new Queue<String>();

        Node startVertex = (Node) nodes.peekFirst();

        // Prepares to search start vertex's neighbours
        next.offer(startVertex);
        // Prevents start vertex from being visited again
        startVertex.wasVisited = true;
        // Adds start vertex to queue of visited nodes
        visited.offer(startVertex.label);

        while (!next.isEmpty()) {
            Node currentVertex = (Node) next.poll();
            Iterator<Node> neighboursIter = currentVertex.neighbours.iterator();
            // Visits neighbours of current vertex
            while (neighboursIter.hasNext()) {
                Node currentNeighbour = 
                    (Node) neighboursIter.next();
                if (!currentNeighbour.wasVisited) {
                    // Prepares to search current neighbour's neighbours
                    next.offer(currentNeighbour);
                    // Prevents current neighbour from being visited again
                    currentNeighbour.wasVisited = true;
                    // Adds current neighbour to queue of visited nodes
                    visited.offer(currentNeighbour.label);
                }
            }
        }
        // Prepares nodes for later reuse
        _markAllUnvisited();

        return visited;
    }

    public Queue<String> dfs() {
        Iterator<Node> nodesIter = nodes.iterator();
        Queue<String> visited = new Queue<String>();

        while (nodesIter.hasNext()) {
            Node currentVertex = (Node) nodesIter.next();
            // Visits neighbours of current vertex
            if (!currentVertex.wasVisited()) {
                _dfsVisit(currentVertex, visited);
            }
        }
        // Prepares nodes for later reuse
        _markAllUnvisited();

        return visited;
    }

    // Adapted from GeeksforGeeks
    // https://www.geeksforgeeks.org/find-paths-given-source-destination/
    // Accessed 07/10/2020
    public void displayPaths(String startVertexLabel, String endVertexLabel) {
        Stack<String> path = new Stack<String>();
        path.push(startVertexLabel);

        Node startVertex = get(startVertexLabel);
        Node endVertex = get(endVertexLabel);
        
        _displayPaths(startVertex, endVertex, path);

        // Prepares nodes for later reuse
        _markAllUnvisited();
    }
    // End of code adapted from GeeksforGeeks

    public void displayList() {
        if (nodes.isEmpty()) {
            throw new IllegalArgumentException("Cannot call displayList on an empty graph");
        }
        else {
            String[][] adjList = _makeAdjList();
            _printArray(adjList);
        }
    }

    public void displayMatrix() {
        if (nodes.isEmpty()) {
            throw new IllegalArgumentException("Cannot call displayMatrix on an empty graph");
        }
        else {
            String[][] adjMatrix = _makeAdjMatrix();
            _printArray(adjMatrix);
        }
    }

    // PRIVATE SUBMODULES

    private void _connect(String inSourceVertexLabel, String inSinkVertexLabel) {
        Iterator<Node> nodesIter = nodes.iterator();
        Node sourceVertex = null;
        Node sinkVertex = null;

        // Finds nodes with inLabel1 and inLabel2
        while (nodesIter.hasNext() && 
            (sourceVertex == null || sinkVertex == null)) {
            Node currentVertex = (Node) nodesIter.next();
            // Marks vertex with label inLabel1 as found
            if (currentVertex.label.equals(inSourceVertexLabel)) {
                sourceVertex = currentVertex;
            }
            // Marks vertex with label inLabel2 as found
            else if (currentVertex.label.equals(inSinkVertexLabel)) {
                sinkVertex = currentVertex;
            }
        }

        if (sourceVertex == null || sinkVertex == null) {
            throw new IllegalArgumentException("Cannot call connect with labels that have not " + 
                "already been assigned to nodes");
        }
        else {
            sourceVertex.addNeighbour(sinkVertex);
            if (!isDirected) {
                sinkVertex.addNeighbour(sourceVertex);
            }
        }
    }

    private boolean _hasNode(String inLabel) {
        Iterator<Node> nodesIter = nodes.iterator();
        boolean hasNode = false;
        while (nodesIter.hasNext() && !hasNode) {
            Node currentVertex = (Node) nodesIter.next();
            if (currentVertex.label.equals(inLabel)) {
                hasNode = true;
            }
        }

        return hasNode;
    }

    private boolean _areNeighbours(String inSourceVertexLabel, String inSinkVertexLabel) {
        Iterator<Node> nodesIter = nodes.iterator();
        boolean areNeighbours = false;
        // Loops through nodes to find vertex with label inLabel1 
        while (nodesIter.hasNext() && !areNeighbours) {
            Node currentVertex = (Node) nodesIter.next();
            // Vertex with label inLabel1 has been found
            if (currentVertex.label.equals(inSourceVertexLabel)) {
                LinkedList<Node> neighbours = currentVertex.neighbours;
                Iterator<Node> neighboursIter = neighbours.iterator();
                // Loops through neighbours to find vertex with label inLabel2
                while (neighboursIter.hasNext() && !areNeighbours) {
                    Node currentNeighbour = 
                        (Node) neighboursIter.next();
                    // Vertex with label inLabel2 has been found
                    if (currentNeighbour.label.equals(inSinkVertexLabel)) {
                        areNeighbours = true;
                    }
                }
            }
        }

        return areNeighbours;
    }

    private Node _getVertex(String inLabel) {
        Iterator<Node> nodesIter = nodes.iterator();
        Node vertex = null;
        while (nodesIter.hasNext() && vertex == null) {
            Node currentVertex = (Node) nodesIter.next();
            if (currentVertex.label.equals(inLabel)) {
                vertex = currentVertex;
            }
        }

        return vertex;
    }

    private int _getNumnodes() {
        Iterator<Node> nodesIter = nodes.iterator();
        int nodeCount = 0;
        while (nodesIter.hasNext()) {
            nodeCount++;
            nodesIter.next();
        }

        return nodeCount;
    }

    private int _getNumEdges() {
        Iterator<Node> nodesIter = nodes.iterator();
        int numEdges = 0;
        while (nodesIter.hasNext()) {
            Node currentVertex = (Node) nodesIter.next();
            Iterator<Node> neighboursIter = currentVertex.neighbours.iterator();
            while (neighboursIter.hasNext()) {
                numEdges++;
                neighboursIter.next();
            }
        }

        if (!isDirected) {
            numEdges /= 2;
        }

        return numEdges;
    }

    private void _markAllUnvisited() {
        Iterator<Node> nodesIter = nodes.iterator();
        while (nodesIter.hasNext()) {
            Node currentVertex = (Node) nodesIter.next();
            currentVertex.wasVisited = false;
        }
    }

    private void _dfsVisit(Node currentVertex, Queue<String> visited) {
        // Prevents vertex from being visited again
        currentVertex.wasVisited = true;
        // Adds current vertex to queue of visited nodes
        visited.offer(currentVertex.label);

        Iterator<Node> neighboursIter = currentVertex.neighbours.iterator();
        while (neighboursIter.hasNext()) {
            Node currentNeighbour = 
                (Node) neighboursIter.next();
            // Visits neighbours of current neighbour
            if (!currentNeighbour.wasVisited()) {
                _dfsVisit(currentNeighbour, visited);
            }
        }
    }

    // Adapted from GeeksforGeeks
    // https://www.geeksforgeeks.org/find-paths-given-source-destination/
    // Accessed 07/10/2020
    private void _displayPaths(Node currentVertex, Node endVertex, Stack<String> localPath) {
        String currentVertexLabel = currentVertex.label;
        String endVertexLabel = endVertex.label;

        // Stops recursing if path is complete
        if (currentVertexLabel.equals(endVertexLabel)) {
            System.out.println(localPath.toString());
        }
        else {
            // Prevents current vertex from being visited again
            currentVertex.wasVisited = true;

            // Visits neighbours of current vertex
            Iterator<Node> neighboursIter = currentVertex.neighbours.iterator();
            while (neighboursIter.hasNext()) {
                Node currentNeighbour = 
                    (Node) neighboursIter.next();
                if (!currentNeighbour.wasVisited()) {
                    localPath.push(currentNeighbour.label);

                    _displayPaths(currentNeighbour, endVertex, localPath);

                    // Prepares to visit next neighbour
                    localPath.pop();
                }
            }

            // Allows current vertex to be visited again
            currentVertex.wasVisited = false;
        }
    }
    // End of code adapted from GeeksforGeeks

    private String[][] _makeAdjList() {
        Iterator<Node> nodesIter = nodes.iterator();
        String[][] adjList = new String[nodeCount][nodeCount];

        for (int i = 0; i < adjList.length; i++) {
            Node currentVertex = (Node) nodesIter.next();
            adjList[i][0] = currentVertex.label;
            Iterator<Node> neighboursIter = currentVertex.neighbours.iterator();
            
            for (int j = 1; j < adjList[0].length; j++) {
                Node currentNeighbour = (Node) neighboursIter.next();
                if (currentNeighbour == null) {
                    adjList[i][j] = "";
                }
                else {
                    adjList[i][j] = currentNeighbour.label;
                }
            }
        }

        return adjList;
    }

    private String[][] _makeAdjMatrix() {
        Iterator<Node> nodesIter = nodes.iterator();
        String[][] adjMatrix = new String[nodeCount + 1][nodeCount + 1];
        adjMatrix[0][0] = " ";

        // Adds y-labels
        for (int i = 1; i < adjMatrix.length; i++) {
            Node currentVertex = (Node) nodesIter.next();
            adjMatrix[i][0] = currentVertex.label;
        }
        nodesIter = nodes.iterator();

        // Adds x-labels
        for (int j = 1; j < adjMatrix[0].length; j++) {
            Node currentVertex = (Node) nodesIter.next();
            adjMatrix[0][j] = currentVertex.label;
        }
        nodesIter = nodes.iterator();

        for (int i = 1; i < adjMatrix.length; i++) {
            String outerCurrentLabel = adjMatrix[i][0];
            for (int j = 1; j < adjMatrix[0].length; j++) {
                String innerCurrentLabel = adjMatrix[0][j];
                if (outerCurrentLabel.equals(innerCurrentLabel)) {
                    adjMatrix[i][j] = "0";
                }
                else if (!areNeighbours(outerCurrentLabel, innerCurrentLabel)) {
                    adjMatrix[i][j] = "0";
                }
                else {
                    adjMatrix[i][j] = "1";
                }
            }
        }

        return adjMatrix;
    }

    private void _printArray(String[][] array) {
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[0].length; j++) {
                System.out.print(" " + array[i][j] + " ");
            }
            System.out.println();
        }
    }
}
