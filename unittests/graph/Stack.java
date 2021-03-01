/*
 * NAME: Stack
 * AUTHOR: Tanaka Chitete
 * PURPOSE: Implement a generic stack
 * CREATION: 06/11/2020
 * LAST MODIFICATION: 09/11/2020
 */

import java.util.*;

public class Stack<E> extends Vector<E> {
    // PRIVATE CLASS FIELDS

    private LinkedList<E> stack;
    private int count;

    // CONSTRUCTORS

    /*
     * DEFAULT CONSTRUCTOR
     * IMPORT(S): NONE
     * EXPORT(S): Address of new Stack object
     * PURPOSE: Create new Stack object
     * CREATION: 03/11/2020
     * LAST MODIFICATION: 09/11/2020
     */

    public Stack() {
        stack = new LinkedList<E>();
    }

    // SETTERS (MUTATORS)

    public boolean push(E element) {
        boolean success;
        if (element == null) {
            success = false;
        }
        else {
            stack.insertFirst(element);
            count++;
            success = true;
        }

        return success;
    }

    // GETTERS (ACCESSORS)

    public E peek() {
        E peekedElement;

        if (isEmpty()) {
            throw new IllegalStateException("Cannot peek at the first element of an empty stack");
        }
        else {
            peekedElement = stack.peekFirst();
        }

        return peekedElement;
    }

    public E pop() {
        E polledElement;
        
        if (isEmpty()) {
            throw new IllegalStateException("Cannot poll at the first element of an empty stack");
        }
        else {
            polledElement = stack.removeFirst();
            count--;
        }

        return polledElement;
    }

    // OPERATORS

    public int size() {
        return count;
    }

    @Override
    public boolean isEmpty() {
        return size() == 0;
    }
}
