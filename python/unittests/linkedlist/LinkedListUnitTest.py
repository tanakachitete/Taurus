"""
NAME: LinkedListUnitTest
AUTHOR: Tanaka Chitete
PURPOSE: Implement a basic unit test for LinkedList
CREATION: 28/02/2021
LAST MODIFICATION: 28/02/2021
"""

from LinkedList import LinkedList

def main():
    numPassed = 0
    numTests = 0
    
# --------------------------------------------------------------------------------------------------
    print("\n\nTesting Normal Conditions - Constructor")
    print("=======================================================================================")

    # TEST 1: CONSTRUCTOR
    try:
        numTests += 1
        linkedList = LinkedList()
        print("Testing creation of LinkedList (isEmpty()): ", end="")
        if not linkedList.isEmpty():
            raise ValueError("Head must be None")
        numPassed += 1
        print("passed")
    except Exception:
        print("FAILED")

# --------------------------------------------------------------------------------------------------
    print("\nTest inserting first and removing first (stack behaviour)")
    print("=======================================================================================")

    # TEST 2: INSERT FIRST
    try:
        numTests += 1
        print("Testing insertFirst(): ", end="")
        linkedList.insertFirst("abc")
        linkedList.insertFirst("jkl")
        linkedList.insertFirst("xyz")
        numPassed += 1
        print("passed")
    except Exception:
        print("FAILED")

    # TEST 3: PEEK LAST
    try:
        numTests += 1
        print("Testing peekLast(): ", end="")
        testString = linkedList.peekLast()
        if testString != "abc":
            raise ValueError("FAILED")
        numPassed += 1
        print("passed")
    except Exception as e:
        print("FAILED")
        print(e)

    # TEST 4: REMOVE FIRST
    try:
        numTests += 1
        print("Testing removeFirst(): ", end="")
        testString = linkedList.removeFirst()
        if testString != "xyz":
            raise ValueError("FAILED")
        testString = linkedList.removeFirst()
        if testString != "jkl":
            raise ValueError("FAILED")
        testString = linkedList.removeFirst()
        if testString != "abc":
            raise ValueError("FAILED")
        numPassed += 1
        print("passed")
    except Exception:
        print("FAILED")

    # TEST 5: IS EMPTY
    try:
        numTests += 1
        print("Testing isEmpty(): ", end="")
        testString = linkedList.removeFirst()
        print("FAILED")
    except Exception:
        numPassed += 1
        print("passed")

# --------------------------------------------------------------------------------------------------

    print("\nTest inserting last and removing first (queue behaviour)")
    print("=======================================================================================")

    # TEST 6: INSERT LAST()
    try:
        numTests += 1
        print("Testing insertLast(): ", end="")
        linkedList.insertLast("abc")
        linkedList.insertLast("jkl")
        linkedList.insertLast("xyz")
        numPassed += 1
        print("passed")
    except Exception:
        print("FAILED")

    # TEST 7: PEEK FIRST
    try:
        numTests += 1
        print("Testing peekFirst(): ", end="")
        testString = linkedList.peekFirst()
        if testString != "abc":
            raise ValueError("FAILED")
        numPassed += 1
        print("passed")
    except Exception:
        print("FAILED")

    # TEST 8: REMOVE FIRST
    try:
        numTests += 1
        print("Testing removeFirst(): ", end="")
        testString = linkedList.removeFirst()
        if testString != "abc":
            raise ValueError("FAILED")
        testString = linkedList.removeFirst()
        if testString != "jkl":
            raise ValueError("FAILED")
        testString = linkedList.removeFirst()
        if testString != "xyz":
            raise ValueError("FAILED")
        numPassed += 1
        print("passed")
    except Exception:
        print("FAILED")

    # TEST 9: IS EMPTY 2
    try:
        numTests += 1
        print("Testing isEmpty(): ", end="")
        testString = linkedList.removeFirst()
        print("FAILED")
    except Exception:
        numPassed += 1
        print("passed")

    # TEST 10: INSERT FIRST
    try:
        numTests += 1
        print("Testing insertFirst(): ", end="")
        linkedList.insertFirst("abc")
        linkedList.insertFirst("jkl")
        linkedList.insertFirst("xyz")
        numPassed += 1
        print("passed")
    except Exception:
        print("FAILED")

# --------------------------------------------------------------------------------------------------
    # PRINT TEST SUMMARY
    print("\nNumber passed: {0}/{1}".format(numPassed, numTests), end="")
    print(" -> {0}%".format((numPassed/numTests) * 100.0))

if __name__ == "__main__":
    main()