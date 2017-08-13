"""Implementation of a deque.

Queue is an ordered collection of items. It has two ends, a front and a rear.
New items can be added at either the front or the rear. Likewise, existing items
can be removed from either end. It provides all the capabilities of stacks and
queues in a single data structure.
"""

from __future__ import division, print_function

__all__ = ['Deque']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-26'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-26'
__version__ = '1.0'


class Deque(object):
    """Implementation of a deque.

    We will use list to build the internal representation of the deque.

    Attributes:
        _items (list)

    >>> d = Deque()
    >>> d.isEmpty()
    True
    >>> d.addRear(4)
    >>> d.addRear('dog')
    >>> d.addFront('cat')
    >>> d.addFront(True)
    >>> d.size()
    4
    >>> d.isEmpty()
    False
    >>> d.addRear(8.4)
    >>> d.removeRear()
    8.4
    >>> d.removeFront()
    True
    """
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []

    def size(self):
        return len(self._items)

    def addRear(self, x):
        self._items.insert(0, x)

    def addFront(self, x):
        self._items.append(x)

    def removeRear(self):
        return self._items.pop(0)

    def removeFront(self):
        return self._items.pop()


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
