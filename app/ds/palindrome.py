"""Palindrome checker.

A palindrome is a string that reads the same forward and backward, such as
radar, toot, and madam. Our goal is to check whether a given string is a
palindrome.
"""

from __future__ import division, print_function

__all__ = ['Palindrome']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-26'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-26'
__version__ = '1.0'

import sys
sys.path.append('../../')
from algds.ds.deque import Deque


class Palindrome(object):
    """Palindrome checker.

    We use a deque to store the characters of the string. After adding each
    character to the rear of the deque, we keep matching the both the front and
    rear.

    Attributes:
        _deque (Deque)

    >>> checker = Palindrome()
    >>> checker.check("lsdkjfskf")
    False
    >>> checker.check("radar")
    True
    >>> checker.check("")
    True
    >>> checker.check("a")
    True
    >>> checker.check("aa")
    True
    >>> checker.check("ab")
    False
    """

    def __init__(self):
        self._deque = None

    def check(self, input_string):
        self._deque = Deque()
        for ch in input_string:
            self._deque.addRear(ch)

        while self._deque.size() > 1:
            if self._deque.removeFront() != self._deque.removeRear():
                return False
        return True


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
