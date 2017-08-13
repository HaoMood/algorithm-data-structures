"""Balanced parentheses checker.

Balanced parentheses means that each opening symbol has a corresponding closing
symbol and the pairs of parentheses are properly nested. For example:
    (()()()), (((()))), (()((())()))

The ability to differentiate between parentheses that are correctly balanced
and those are unbalanced is an import part of recognizing many programming
language structures.

Applications: Parentheses are used in arithmetic expressions to order the
performance of operations. Lots and lots of parentheses are used in Lisp syntax.
"""

from __future__ import division, print_function

__all__ = ['ParenChecker']
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


class ParenChecker(object):
    """Read a string of parentheses decide whether they symbols are balanced.

    Observation: the most recent opening parenthesis must match the next closing
    symbol. Also, the first opening symbol processed may have to wait until the
    very last symbol for its match. Closing symbols match opening symbols in the
    reverse order of their appearance; they match from the inside out. This is
    a clue that stacks can be used to solve the problem.

    Starting with an empty stack, process the parenthesis strings from left to
    right. If a symbol is an opening parenthesis, push it on the stack as a
    signal that a corresponding closing symbol needs to appear later. If, on the
    other hand, a symbol is a closing parenthesis, pop the stack. As long as it
    is possible to pop the stack to match every closing symbol, the parentheses
    remain balanced. At the end of the string, the stack should be empty.

    >>> checker = ParenChecker()
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
    """

    def __init__(self):
        self._stack = None

    def isBalance(self, symbol_string):
        self._checkValid(symbol_string)
        self._stack = Stack()

        for ch in symbol_string:
            if ch == '(':
                self._stack.push(ch)
            else:  # ch == ')'
                if self._stack.isEmpty():
                    return False
                else:
                    self._stack.pop()

        return self._stack.isEmpty()

    def _checkValid(self, symbol_string):
        if not isinstance(symbol_string, str):
            raise ValueError('The argument should be a string.')
        for ch in symbol_string:
            if not (ch == '(' or ch == ')'):
                raise ValueError('Only "(" and ")" are allowed characters.')


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
