"""Implementation of a priority queue.

A priority queue acts like a queue in that you dequeue an item by removing it
from the front. However, in a priority queue the logical order of items inside
a queue is determined by their priority. The highest prioprity items are at the
front of the queue and the lowest priority items are at the back.
"""

from __future__ import division, print_function

__all__ = ['PriorityQueue']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-08-12'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-08-12'
__version__ = '1.0'


class PriorityQueue(object):
    """Implementation of a priority queue using a binary min heap.

    A binary heap will allow us both enqueue and dequeue items in O(lg n).

    >>> priority_queue = PriorityQueue()
    >>> priority_queue.insert(5)
    >>> priority_queue.insert(7)
    >>> priority_queue.insert(3)
    >>> priority_queue.insert(11)
    >>> print(priority_queue.delMin())
    3
    >>> print(priority_queue.delMin())
    5
    >>> print(priority_queue.delMin())
    7
    >>> print(priority_queue.delMin())
    11
    """
    def __init__(self):
        # An empty binary heap has a single zero as the first element, and that
        # this zero is not used, but is there so that simple integer division
        # can be used in later methods.
        self._heap = [0]
        self._current_size = 0

    def insert(self, key):
        """Add an item to the heap."""
        self._heap.append(key)
        self._current_size += 1
        self._heapify(self._current_size)

    def _heapify(self, i):
        """Heapify a new item as far up in the tree as it needs to go to
        maintain the heap property.

        When we percolate an item up, we are restoring the heap property between
        the newly added item and the parent. If the newly added item is less
        than its parent, then we can swap the item with its parent.
        """
        while i // 2 > 0:
            if self._heap[i] < self._heap[i // 2]:
                self._heap[i], self._heap[i // 2] = (self._heap[i // 2],
                                                     self._heap[i])
            i //= 2

    def delMin(self):
        """Remove the smallest and heapfity the heap.

        First, we will restore the root item by taking the last item in the list
        and moving it to the root position. Moving the last item maintains our
        heap structure property.

        Second, we will restore the heap order property by pushing the new root
        node down the tree to its proper position. In order to maintain the heap
        order property, all we need to do is swap the root with its smallest
        child less than the root.
        """
        retrieval = self._heap[1]
        self._heap[1] = self._heap[self._current_size]
        self._current_size -= 1
        self._heap.pop()
        self._percDown(1)
        return retrieval

    def _percDown(self, i):
        while i * 2 <= self._current_size:
            min_child = self._minChild(i)
            if self._heap[i] > self._heap[min_child]:
                self._heap[i], self._heap[min_child] = (self._heap[min_child],
                                                        self._heap[i])
            i = min_child

    def _minChild(self, i):
        if i * 2 + 1 > self._current_size:
            return i * 2
        elif self._heap[i * 2] < self._heap[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

    def build(self, aList):
        """Build an entire heap from a list of keys in O(n) time."""
        i = len(aList) // 2
        self._current_size = len(aList)
        self._heap = [0] + aList[:]
        # Any nodes past the halfway point will be leaves and therefore have no
        # children.
        while i > 0:
            self._percDown(i)
            i -= 1


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
