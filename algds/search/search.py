"""Linear search and binary search."""

from __future__ import division, print_function

__all__ = ['Search']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-28'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-28'
__version__ = '1.0'


class Search(object):
    """Sequential search through a list.

    >>> s = Search([1, 2, 32, 8, 17, 19, 42, 13, 0])
    >>> s.linear(3)
    False
    >>> s.linear(13)
    True
    >>> s = Search(sorted([1, 2, 32, 8, 17, 19, 42, 13, 0]))
    >>> s.binary(3)
    False
    >>> s.binary(13)
    True
    >>> s = Search([1])
    >>> s.binary(1)
    True
    >>> s.binary(2)
    False
    >>> s = Search([])
    >>> s.binary(1)
    False
    """

    def __init__(self, list_):
        self._list = list_

    def linear(self, x):
        for val in self._list:
            if val == x:
                return True
        return False

    def binary(self, x):
        low = 0
        high = len(self._list)
        mid = (low + high) // 2
        while mid != high:
            if x == self._list[mid]:
                return True
            elif x < self._list[mid]:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        return False


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
