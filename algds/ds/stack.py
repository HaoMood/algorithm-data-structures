"""Implementation of a stack.

Stack is an ordered collection of items where the addition of new items and the
removal of existing items always takes place at the same end. This end is
commonly referred to as the "top". The end opposite the top is known as the
"base".

The ordering principle is called last-in, first-out (LIFO). Newer items are near
the top, while older items are near the base.

Applications: Every web browser has a back button. As you navigate from web
page to web page, those URLs are placed on a stack. The current page that you
are viewing is on the top.
"""

from __future__ import division, print_function

__all__ = ["Stack"]
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-25'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-25'
__version__ = '1.0'


class Stack(object):
    """Implementation of a stack.

    The stack is implemented by a list, and the end of the list will hold the
    top element of the stack.

    Attributes:
        _items (list): Used to store items in the stack.

    >>> s = Stack()
    >>> s.isEmpty()
    True
    >>> s.push(4)
    >>> s.push('dog')
    >>> s.top()
    'dog'
    >>> s.push(True)
    >>> s.size()
    3
    >>> s.isEmpty()
    False
    >>> s.push(8.4)
    >>> s.pop()
    8.4
    >>> s.pop()
    True
    >>> s.size()
    2
    """

    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []

    def push(self, x):
        self._items.append(x)

    def pop(self):
        return self._items.pop()

    def top(self):
        return self._items[self.size() - 1]

    def size(self):
        return len(self._items)


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
