"""Converting decimal numbers to any base.

The dec2bin module is a specific case of this module. The idea is to divide
the decimal number by the base and uses a stack to keep track of the digits for
the result. The first remainder we compute will actually be the last digit in
the sequence. The divide by base algorithm assumes that we start with an
integer greater than 0. The reversal property that signals that a stack a
likely to be the appropriate data structure for solving the problem.
"""

from __future__ import division, print_function

__all__ = ["BaseConverter"]
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


class BaseConverter(object):
    """Converting decimal numbers to any base.

    Attributes:
        _stack (Stack): Used to store the remainders.
        _dec_number (int > 0): The decimal number to be converted.

    >>> converter = BaseConverter()
    >>> converter.convert(233)
    '11101001'
    >>> converter.convert(0)
    '0'
    >>> converter.convert(1)
    '1'
    >>> converter.convert(2)
    '10'
    >>> converter.convert(-1)
    Traceback (most recent call last):
    ...
    ValueError: Argument should >= 0.
    >>> converter.convert(233, base=8)
    '351'
    >>> converter.convert(233, base=16)
    'E9'
    >>> converter.convertRec(233)
    '11101001'
    >>> converter.convertRec(0)
    '0'
    >>> converter.convertRec(1)
    '1'
    >>> converter.convertRec(2)
    '10'
    >>> converter.convertRec(-1)
    Traceback (most recent call last):
    ...
    ValueError: Argument should >= 0.
    >>> converter.convertRec(233, base=8)
    '351'
    >>> converter.convertRec(233, base=16)
    'E9'
    """
    def __init__(self):
        self._stack = None
        self._dec_number = None
        self._digits = '0123456789ABCDEF'

    def convert(self, dec_number, base=2):
        """Converting decimal numbers to binary numbers.

        Args:
            dec_number (str/int): Decimal representation of a number >= 0.
            base (int [2, 16]) [2]: Base of the convertion.

        Returns:
            (str): Representation in base of dec_number.

        Raises:
            ValueError: If the argument is not valid.
        """
        self._dec_number = self._checkValid(dec_number)
        if self._dec_number == 0:
            return '0'
        if not isinstance(base, int) or base > 16 or base < 2:
            raise ValueError('Base should be int in range [2, 16].')

        self._stack = Stack()
        while self._dec_number > 0:
            self._dec_number, rem = divmod(self._dec_number, base)
            self._stack.push(rem)

        bin_number = []
        while not self._stack.isEmpty():
            bin_number.append(self._digits[self._stack.pop()])
        return ''.join(bin_number)

    def convertRec(self, dec_number, base=2):
        """Converting decimal numbers to binary numbers using recursion.

        Args:
            dec_number (str/int): Decimal representation of a number >= 0.
            base (int [2, 16]) [2]: Base of the convertion.

        Returns:
            (str): Representation in base of dec_number.

        Raises:
            ValueError: If the argument is not valid.
        """
        self._dec_number = self._checkValid(dec_number)
        if self._dec_number == 0:
            return '0'
        if not isinstance(base, int) or base > 16 or base < 2:
            raise ValueError('Base should be int in range [2, 16].')

        if dec_number < base:
            return self._digits[dec_number]
        else:
            return (self.convertRec(dec_number // base, base)
                    + self._digits[dec_number % base])

    def _checkValid(self, args):
        if isinstance(args, str):
            args = int(args)
        if not isinstance(args, int):
            raise ValueError("Argument should be str/int type.")
        if args < 0:
            raise ValueError("Argument should >= 0.")
        return args


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
