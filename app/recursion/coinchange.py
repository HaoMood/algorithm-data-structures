"""Making change using the fewest coins.

Sometimes the greedy strategy works: start with the largest coin in our
arsenal, and use as many as those as possible, then we go to the next lowest
coin value and use as many of those as possible.

We can use dynamic programming to find the best strategy.
"""

from __future__ import division, print_function

__all__ = ['Coin']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-28'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-28'
__version__ = '2.0'  # Bottom-up dynamic programming


import sys

class Coin(object):
    """Making change using the fewest coins.

    Attributes:
        _coin_values (list of int/float): Coin values we have.
        _change (int/float): Value you want to make change.
        _min_number (list of int): The minimum number of coins available to make
            changes.
        _opt_first_coin (list of int/float): The first coin you make to get the
            optimal changes.

    >>> c = Coin([1, 5, 10, 25])
    >>> c.minCoins(1)
    1
    >>> c.makeChange()
    [1]
    >>> c.minCoins(4)
    4
    >>> c.makeChange()
    [1, 1, 1, 1]
    >>> c.minCoins(6)
    2
    >>> c.makeChange()
    [1, 5]
    >>> c.minCoins(15)
    2
    >>> c.makeChange()
    [5, 10]
    >>> c.minCoins(35)
    2
    >>> c.makeChange()
    [10, 25]
    """

    def __init__(self, coin_values):
        self._coin_values = coin_values
        self._change = None
        self._min_number = None
        self._opt_first_coin = None

    def minCoins(self, change):
        self._change = change
        self._min_number = [sys.maxsize] * (change + 1)
        self._min_number[0] = 0
        self._opt_first_coin = [None] * (change + 1)
        for value in xrange(1, change + 1):
            for coin in [x for x in self._coin_values if x <= value]:
                if 1 + self._min_number[value - coin] < self._min_number[value]:
                    self._min_number[value] = 1 + self._min_number[value - coin]
                    self._opt_first_coin[value] = coin
        return self._min_number[change]

    def makeChange(self):
        change = self._change
        change_list = []
        while change > 0:
            change_list.append(self._opt_first_coin[change])
            change -= self._opt_first_coin[change]
        return change_list

def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
