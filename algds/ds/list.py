"""Implementation of a unordered/ordered single linked list.

An unordered single linked list is a collection of items where each item holds a
relative position wrt the others. There is no requirement that we maintain that
positioning in contiguous memory.

The first item of a linked list is head. Similarly, the last item needs to know
that there is no next item.
"""

from __future__ import division, print_function

__all__ = ['UnorderedList', 'OrderedList']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-27'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-27'
__version__ = '1.0'


class Node(object):
    """The basic building block for the linked list.

    Attributes:
        data: Contain the list item.
        next (Node): Reference to the next Node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class UnorderedList(object):
    """Implementation of an unordered list.

    It contains a collection of nodes, each linked to the next by explicit
    references. The trick is, we use the head as the sentinel element.

    Attributes:
        _head (Node): Reference to the first node.

    >>> l = UnorderedList()
    >>> l.isEmpty()
    True
    >>> l.size()
    0
    >>> l.append(31)
    >>> l.isEmpty()
    False
    >>> l.size()
    1
    >>> l.add(77)
    >>> l.add(17)
    >>> l.add(93)
    >>> l.add(26)
    >>> l.append(54)
    >>> l.isEmpty()
    False
    >>> l.size()
    6
    >>> l.contains(17)
    True
    >>> l.contains(31)
    True
    >>> l.contains(54)
    True
    >>> l.contains(100)
    False
    >>> l.remove(31)
    >>> l.remove(54)
    >>> l.size()
    4
    """

    def __init__(self):
        self._head = Node(None)

    def isEmpty(self):
        return self._head.next is None

    def add(self, x):
        """Add the item x to the right of the head.

        Args:
            x: Item to be added.
        """
        node = Node(x)
        node.next = self._head.next
        self._head.next = node

    def contains(self, x):
        p = self._head.next
        while p is not None and p.data != x:
            p = p.next
        if p is None:
            return False
        else:
            return True

    def size(self):
        count = 0
        p = self._head.next
        while p is not None:
            count += 1
            p = p.next
        return count

    def remove(self, x):
        """Remove the item x.

        The trick is to use two external references as we traverse down the
        linked list.

        Args:
            x: Item to be removed.

        Raises:
            ValueError: If x is not in the list.
        """
        p_current = self._head.next
        p_prev = self._head
        while p_current is not None and p_current.data != x:
            p_prev = p_current
            p_current = p_current.next

        if p_current is None:
            raise ValueError('{} is not contained in the list.'.format(x))
        else:
            p_prev.next = p_current.next

    def append(self, x):
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = Node(x)


class OrderedList(object):
    """Implementation of an ordered list.

    It contains a collection of nodes, each linked to the next by explicit
    references. The relative order of the elements are presered. The trick is,
    we use the head as the sentinel element.

    Attributes:
        _head (Node): Reference to the first node.

    >>> l = OrderedList()
    >>> l.isEmpty()
    True
    >>> l.size()
    0
    >>> l.add(31)
    >>> l.isEmpty()
    False
    >>> l.size()
    1
    >>> l.add(77)
    >>> l.add(17)
    >>> l.add(93)
    >>> l.add(26)
    >>> l.add(54)
    >>> l.isEmpty()
    False
    >>> l.size()
    6
    >>> l.contains(17)
    True
    >>> l.contains(93)
    True
    >>> l.contains(54)
    True
    >>> l.contains(44)
    False
    >>> l.remove(31)
    >>> l.remove(54)
    >>> l.size()
    4
    """

    def __init__(self):
        self._head = Node(None)

    def isEmpty(self):  # Same as UnorderedList
        return self._head.next is None

    def add(self, x):
        """Add the item x to the correct position in the list.

        Args:
            x: Item to be added.
        """
        p = self._head
        while p.next is not None and p.next.data < x:
            p = p.next

        node = Node(x)
        if p.next is not None:
            node.next = p.next
        p.next = node

    def contains(self, x):
        p = self._head.next
        while p is not None and p.data < x:
            p = p.next
        if p is None or p.data > x:
            return False
        else:
            return True

    def size(self):  # Same as UnorderedList
        count = 0
        p = self._head.next
        while p is not None:
            count += 1
            p = p.next
        return count

    def remove(self, x):
        """Remove the item x.

        The trick is to use two external references as we traverse down the
        linked list.

        Args:
            x: Item to be removed.

        Raises:
            ValueError: If x is not in the list.
        """
        p_current = self._head.next
        p_prev = self._head
        while p_current is not None and p_current.data < x:
            p_prev = p_current
            p_current = p_current.next

        if p_current is None or p_current.data != x:
            raise ValueError('{} is not contained in the list.'.format(x))
        else:
            p_prev.next = p_current.next

    def __str__(self):
        elements = []
        p = self._head.next
        while p is not None:
            elements.append(str(p.data))
            p = p.next
        return ', '.join(elements)


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
