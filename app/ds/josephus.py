"""Simulation of the Josephus problem.

In the Hot Potato game, children line up in a circle and pass an item from
neighbor to neighbor as fast as they can. At a certain point in the game, the
action is stopped and the child who has the item (the potato) is removed from
the circle. Play continues until only one child is left.

In the Josephus problem, 40 people arrange themselves in a circle. One man was
designated as number one, and proceeding clockwise they killed every seventh
man. Play continues until only one child is left.
"""

from __future__ import division, print_function

__all__ = ['Josephus']
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
from algds.ds.queue import Queue


class Josephus(object):
    """Simulation of the Josephus problem.

    Input a list of names and a constance called num to be used for counting.
    It will return the name of the last person remaining after repetitive
    counting by num.

    To simulate the circle, we will use a queue. Assume the number one person is
    at the front of the queue. Upon passing the potato, the simulation will
    simply dequeue and then immediately enqueue that child, putting her at the
    end of the line. After num dequeue/enqueue operations, the child at the
    front will be removed permanently and another cycle will begin.

    >>> jose = Josephus()
    >>> jose.simulate(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
    'Kent'
    """
    def __init__(self):
        self._queue = None

    def simulate(self, name_list, num):
        if not isinstance(num, int) or num < 1:
            raise ValueError('num should be int > 1.')

        self._queue = Queue()
        for name in name_list:
            self._queue.enqueue(name)

        while self._queue.size() > 1:
            for _ in xrange(num - 1):
                self._queue.enqueue(self._queue.dequeue())
            self._queue.dequeue()

        return self._queue.dequeue()


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
