/*
 * NAME: Set
 * AUTHOR: Tanaka Chitete
 * PURPOSE: Implement generic Set
 * CREATION: 22/09/2020
 * LAST MODIFICATION: 02/03/2021
 */

import java.util.*;

public class Set<E> extends AbstractSet<E> {
    // PRIVATE CLASS FIELDS

    private HashMap<E, E> entries;

    // CONSTRUCTORS

    /*
     * CONSTRUCTOR
     * IMPORT(S): NONE
     * EXPORT(S): Address of new Set
     * PURPOSE: Create new Set
     * CREATION: 22/10/2020
     * LAST MODIFICATION: 02/03/2021
     */

    public Set() {
        this.entries = new HashMap<E, E>();
    }

    // SETTERS (MUTATORS)

    @Override
    public boolean add(E element) {
        this.entries.put(element, element);
        return true; // put() always associates K with V
    }

    // GETTERS (ACCESSORS)

    @Override
    public boolean contains(Object element) {
        return this.entries.containsKey(element);
    }

    @Override
    public boolean remove(Object element) {
        return this.entries.remove(element, element);
    }

    @Override
    public int size() {
        return this.entries.size();
    }

    // OPERATORS

    @Override
    public Iterator<E> iterator() {
        throw new UnsupportedOperationException();
    }

    @Override
    public String toString() {
        return this.entries.values().toString();
    }

    @Override
    public boolean isEmpty() {
        return this.entries.isEmpty();
    }
}
