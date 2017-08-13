#!/usr/bin/env python
"""The tower of Hanoi problem.

The priests were given three poles and a stack of 64 disks, each disk is a
little smaller than the one beneath it. The assignment was to transfer all 64
disks from one of the three poles to another. The constriant is that we could
only move one disk at a time, and we could never place a larger disk on top of
a smaller one.
"""

from __future__ import division, print_function

__all__ = ['Hanoi']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-27'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-27'
__version__ = '1.0'


class Hanoi(object):
    """The tower of Hanoi problem.

    Attributes
        _from (str): Identification of the from pole.
        _to (str): Identification of the to pole.
        _via (str): Identification of the via pole.
    """

    def __init__(self, from_, to, via):
        self._from = from_
        self._to = to
        self._via = via

    def solve(self, height=64):
        if not isinstance(height, int):
            raise ValueError('height should be int.')
        self._move(self._from, self._to, self._via, height)

    def _move(self, from_, to, via, height):
        if height <= 0:
            return
        self._move(from_, via, to, height - 1)  # Move top height-1 to via.
        print('{} -> {}'.format(from_, to))     # Move from to to.
        self._move(via, to, from_, height - 1)  # Move via to to.


def main():
    h = Hanoi('A', 'B', 'C')
    print('-' * 80)
    h.solve(1)
    print('-' * 80)
    h.solve(2)
    print('-' * 80)
    h.solve(3)
    print('-' * 80)
    h.solve(4)
    print('-' * 80)


if __name__ == '__main__':
    main()
