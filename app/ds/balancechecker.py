"""Balanced symbol checker.

The module parenchecker is a specific case of this module. The general problem
of balancing nesting and nesting different kinds of opening and closing symbols
occurs frequently. For examples, the followings are balanced since each opening
symbol have a corresponding closing symbol, but the types of symbols match as
well:
    {{([][])}()}, [[{{(())}}]], [][][](){},
and the followings are not balanced:
    ([)], ((()])), [{()]
"""

from __future__ import division, print_function

__all__ = ['BalanceChecker']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-25'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-25'
__version__ = '1.0'

import sys
sys.path.append('../../')
from algds.ds.stack import Stack


class BalanceChecker(object):
    """Read a string of symbols and decide whether they are balanced.

    Starting with an empty stack, process the symbol strings from left to
    right.  If a symbol is an opening symbol, push it on the stack as a signal
    that a corresponding closing symbol needs to appear later. If, on the other
    hand, a symbol is a closing symbol, we need to check that it correctly
    matches the type of the opening symbol on top of the stack. At the end of
    the string, the stack should be empty.

    Attributes:
        _stack (Stack): Used to store open symbols
        _

    >>> checker = BalanceChecker('([{', ')]}')
    >>> checker.isBalance('((()))')
    True
    >>> checker.isBalance('(()')
    False
    >>> checker.isBalance('')
    True
    >>> checker.isBalance('(')
    False
    >>> checker.isBalance(')')
    False
    >>> checker.isBalance('{{([][])}()}')
    True
    >>> checker.isBalance('[{()]')
    False
    """

    def __init__(self, open_symbols, close_symbols):
        if (not isinstance(open_symbols, str) or
            not isinstance(close_symbols, str)):
            raise ValueError('Open and close symbols should be str type.')
        if len(open_symbols) != len(close_symbols):
            raise ValueError('Open and close symbols do not match.')

        self._stack = None
        self._open_symbols = open_symbols
        self._close_symbols = close_symbols

    def isBalance(self, symbol_string):
        self._checkValid(symbol_string)
        self._stack = Stack()

        for ch in symbol_string:
            if ch in self._open_symbols:
                self._stack.push(ch)
            elif self._stack.isEmpty():  # ch in self._close_symbols
                return False
            else:
                top = self._stack.pop()
                # Check whether the symbol popped matches the type of current.
                if (self._open_symbols.index(top) !=
                    self._close_symbols.index(ch)):
                    return False

        return self._stack.isEmpty()

    def _checkValid(self, symbol_string):
        if not isinstance(symbol_string, str):
            raise ValueError('The argument should be a string.')
        for ch in symbol_string:
            if not (ch in self._open_symbols or ch in self._close_symbols):
                raise ValueError('Only %s and %s are allowed characters.' %
                                 self._open_symbols, self._close_symbols)


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
