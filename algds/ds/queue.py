"""Implementation of a queque.

Queue is an ordered collection of items where the addition of new item happens
at one end called the rear, and the removal of existing items occurs at the
other end called the front. This ordering principle is called FIFO, first-in
first-out.

Applications: When 30 computers networked with a single printer, the first task
in is the next to be completed. Operating systems use a number of different
queues to control processes within a computer. The scheduler tries to execute
programs as quickly as possible and serve as many users as it can.
"""

from __future__ import division, print_function

__all__ = ['Queue']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-26'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-25'
__version__ = '1.0'


class Queue(object):
    """Implementation of a queque.

    We will use list to build the internal representation of the queue. Assume
    that the rear is at position 0 in the list, and the last element is the
    front.

    Attributes:
        _items (list):

    >>> q = Queue()
    >>> q.isEmpty()
    True
    >>> q.enqueue(4)
    >>> q.enqueue('dog')
    >>> q.enqueue(True)
    >>> q.size()
    3
    >>> q.isEmpty()
    False
    >>> q.enqueue(8.4)
    >>> q.dequeue()
    4
    >>> q.dequeue()
    'dog'
    >>> q.size()
    2
    """
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []

    def size(self):
        return len(self._items)

    def enqueue(self, x):
        self._items.insert(0, x)

    def dequeue(self):
        return self._items.pop()


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
