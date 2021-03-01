/*
 * NAME: Set
 * AUTHOR: Tanaka Chitete
 * PURPOSE: Implement a generic Set
 * CREATION: 22/09/2020
 * LAST MODIFICATION: 09/11/2020
 */

import java.util.*;

public class Set<E> extends AbstractSet<E> {
    // NESTED CLASSES

    private class Element<A> {    
        // PRIVATE CLASS FIELDS
    
        private A element;
        private int state;
    
        // CONSTRUCTORS
    
        /*
         * DEFAULT CONSTRUCTOR
         * IMPORT(S): NONE
         * EXPORT(S): Address of new Element
         * PURPOSE: Create new Element in default state
         * CREATION: 22/09/2020
         * LAST MODIFICATION: 22/10/2020
         */
    
        private Element() {
            element = null;
            state = NEVER_USED;
        }
    
        /*
         * ALTERNATE CONSTRUCTOR
         * IMPORT(S): inElement (String)
         * EXPORT(S): Address of new DSAHashTableEntry
         * PURPOSE: Create new DSAHashTableEntry in alternate state
         * CREATION: 26/09/2020
         * LAST MODIFICATION: 22/10/2020
         */
    
        private Element(A inElement) {
            element = inElement;
            state = IN_USE;
        }
    }

    // PRIVATE CLASS CONSTANTS

    private static final int USABLE_CAPACITY = 5;
    private static final int REAL_CAPACITY = 7;

    private static final int IN_USE = 0;
    private static final int WAS_USED = 1;
    private static final int NEVER_USED = 2;

    // PRIVATE CLASS FIELDS

    private Element<E>[] entries;
    private int count;

    // CONSTRUCTORS

    /*
     * DEFAULT CONSTRUCTOR
     * IMPORT(S): NONE
     * EXPORT(S): Address of new DSAHashSet
     * PURPOSE: Create new DSAHashSet in default state
     * CREATION: 22/10/2020
     * LAST MODIFICATION: 22/10/2020
     */

    @SuppressWarnings("unchecked")
    public Set() {
        entries = new Element[REAL_CAPACITY];
        count = 0;

        // Instantiates entries
        for (int i = 0; i < entries.length; i++) {
            entries[i] = new Element<E>();
        }
    }

    // SETTERS (MUTATORS)

    @Override
    public boolean add(E inElement) {
        boolean wasAdded;

        if (isFull()) {
            throw new IllegalStateException("Cannot call add on a full Set");
        }
        else if (inElement == null) {
            throw new IllegalArgumentException("Cannot call add with a null element");
        }
        else {
            // Checks if element is already in the set
            int foundEntryHash = _find(inElement);
            if (foundEntryHash != -1) {
                wasAdded = false;
            }
            // Adds element to the set
            else {
                _add(inElement);
                count++;
                wasAdded = true;
            }
        }

        return wasAdded;
    }

    // GETTERS (ACCESSORS)

    @Override
    public boolean contains(Object inElement) {
        boolean doesContain;
        
        if (inElement == null) {
            doesContain = false;
        }
        else {
            // Checks if element is already in the set
            int foundEntryHash = _find(inElement);
            if (foundEntryHash == -1) {
                doesContain = false;
            }
            else {
                doesContain = true;
            }
        }

        return doesContain;
    }

    @Override
    public boolean remove(Object inElement) {
        boolean wasRemoved;

        if (isEmpty()) {
            throw new IllegalStateException("Cannot call remove on an empty Set");
        }
        else if (inElement == null) {
            wasRemoved = false;
        }
        else {
            int foundEntryHash = _find(inElement);
            if (foundEntryHash == -1) {
                wasRemoved = false;
            }
            else {
                // Reinstantiates entry of previously found element
                entries[foundEntryHash].element = null;
                entries[foundEntryHash].state = WAS_USED;
                count--;
                wasRemoved = true;
            }
        }

        return wasRemoved;
    }

    @Override
    public int size() {
        return count;
    }

    public int capacity() {
        return entries.length;
    }

    public double load() {
        return (double) size() / (double) capacity();
    }

    // OPERATORS

    public boolean isEmpty() {
        return (count == 0);
    }

    public boolean isFull() {
        return (count == USABLE_CAPACITY);
    }

    public String toString() {
        String elementsString = "[";
        int remainingElements = count;
        if (count != 0) {
            for (int i = 0; i < entries.length; i++) {
                Element<E> currentEntry = entries[i];
                if (currentEntry.element != null) {
                    if (remainingElements == 1) {
                        elementsString += "\"" + currentEntry.element + "\"";
                        remainingElements--;
                    }
                    else {
                        elementsString += "\"" + currentEntry.element + "\", ";
                        remainingElements--;
                    }   
                }
            }
        }
        elementsString += "]";

        return elementsString;
    }

    // ITERATOR

    @Override
    public Iterator<E> iterator() {
        throw new UnsupportedOperationException();
    }

    // PRIVATE SUBMODULES

    private void _add(E inElement) {
        String inElementString = inElement.toString();

        int hash = _hash(inElementString);
        int step = _toStep(hash);

        boolean foundFreeSlot = false;
        while (!foundFreeSlot) {
            // Prepares to stop if free slot has been found
            if (entries[hash].state != IN_USE) {
                foundFreeSlot = true;
            }
            // Continues probing for free slot
            else {
                hash += step;
                hash %= entries.length;
            }
        }

        // Adds new entry at previously found free slot
        Element<E> newElement = new Element<E>(inElement);
        entries[hash] = newElement;
    }

    private int _find(Object inElement) {
        String inElementString = inElement.toString();

        int hash = _hash(inElementString);
        int originalHash = hash;
        int step = _toStep(hash);

        boolean foundElement = false;
        boolean checkedAllEntries = false;
        while (!foundElement && !checkedAllEntries) {
            // Prepares to stop if entry was never used
            if (entries[hash].state == NEVER_USED) {
                checkedAllEntries = true;
            }
            // Checks if current element is a match
            else if (Objects.equals(entries[hash].element, inElement)) {
                foundElement = true;
            }
            // Continues probing for target element
            else {
                hash += step;
                hash %= entries.length;
                // Prepares to stop if all entries have been checked
                if (hash == originalHash) {
                    checkedAllEntries = true;
                }
            }
        }

        // Signals that element is not present in the set 
        if (!foundElement) {
            hash = -1;
        }

        return hash;
    }

    private int _hash(String inElement) {
        long inElementHashLong = 0;

        for (int i = 0; i < inElement.length(); i++) {
            inElementHashLong += (31 * inElementHashLong) + (long) inElement.charAt(i);
        }
        int inElementHashInt = (int) (inElementHashLong % (long) entries.length);

        return inElementHashInt;
    }

    private int _toStep(int valueHash) {
        return 5 - (valueHash % 5);
    }
}
