"""Converting decimal numbers to binary numbers.

The idea is to divide the decimal number by 2 and uses a stack to keep track
of the digits for the binary result. The first remainder we compute will
actually be the last digit in the sequence. The divide by 2 algorithm assumes
that we start with an integer greater than 0. The reversal property that signals
that a stack a likely to be the appropriate data structure for solving the
problem.
"""

from __future__ import division, print_function

__all__ = ["Dec2Bin"]
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-26'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-25'
__version__ = '1.0'

import sys
sys.path.append('../../')
from algds.ds.stack import Stack


class Dec2Bin(object):
    """Converting decimal numbers to binary numbers.

    Attributes:
        _stack (Stack): Used to store the remainders.
        _dec_number (int > 0): The decimal number to be converted.

    >>> dec2bin = Dec2Bin()
    >>> dec2bin.convert(233)
    '11101001'
    >>> dec2bin.convert(0)
    '0'
    >>> dec2bin.convert(1)
    '1'
    >>> dec2bin.convert(2)
    '10'
    >>> dec2bin.convert(-1)
    Traceback (most recent call last):
    ...
    ValueError: Argument should >= 0.
    """
    def __init__(self):
        self._stack = None
        self._dec_number = None

    def convert(self, dec_number):
        """Converting decimal numbers to binary numbers.

        Args:
            dec_number (str/int): Decimal representation of a number >= 0.

        Returns:
            (str): Decimal representation of dec_number.

        Raises:
            ValueError: If the argument is not valid.
        """
        self._checkValid(dec_number)
        if self._dec_number == 0:
            return '0'

        self._stack = Stack()
        while self._dec_number > 0:
            self._dec_number, rem = divmod(self._dec_number, 2)
            self._stack.push(rem)

        bin_number = []
        while not self._stack.isEmpty():
            bin_number.append(str(self._stack.pop()))
        return ''.join(bin_number)

    def _checkValid(self, dec_number):
        if isinstance(dec_number, str):
            dec_number = int(dec_number)
        if not isinstance(dec_number, int):
            raise ValueError("Argument should be str/int type.")
        if dec_number < 0:
            raise ValueError("Argument should >= 0.")
        self._dec_number = dec_number


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
