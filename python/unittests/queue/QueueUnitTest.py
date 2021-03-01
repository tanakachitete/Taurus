"""
NAME: QueueUnitTest
AUTHOR: Tanaka Chitete
PURPOSE: Implement a basic unit test for Queue
CREATION: 01/03/2021
LAST MODIFICATION: 01/03/2021
"""

from Queue import Queue

def main():
    try:
        # Instantiation
        queue = Queue()

        # Accessors and Mutators
        print("enqueue Test (View code)")
        enqueueTest(queue, 100)
        print("Number of elements: {0}".format(len(queue)))
        print("peek Test\nElement 0: {0}".format(queue.peek()))
        print("dequeue Test\nFRONT OF THE QUEUE")
        dequeueTest(queue)
        print("BACK OF THE QUEUE")
    except RuntimeError as e:
        print(e)
    except AttributeError as e:
        print(e)

def enqueueTest(queue, numPushElements):
    for i in range(numPushElements):
        queue.enqueue(i)

def dequeueTest(queue):
    for i in range(len(queue)):
        print("Element {0}: {1}".format(i, queue.dequeue()))

if __name__ == "__main__":
    main()