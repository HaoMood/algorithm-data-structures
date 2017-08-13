#!/usr/bin/env python
"""Simulation of printing tasks.

Students send printing tasks to the shared printer, the tasks are placed in a
queue. We are concerned about whether the printer is capable of handling a
certain amount of work. That is to say, the average amount of time students
will wait for their papers to be printed.

Say on any average data about 10 students are working in the lab at any given
hour. These students typically print twice during that time, and length of
these tasks ranges from 1 to 20 pages uniformly. The chance that at any given
second, a print task is going to be created is 20 tasks/hour = 1/180
task/second.
"""

from __future__ import division, print_function

__all__ = ['Simulation']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-26'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-26'
__version__ = '1.0'

import random
import sys

sys.path.append('../../')
from algds.ds.queue import Queue


class _Printer(object):
    """_Printer which needs to track whether it has a current task.

    If it does, then it is busy and the amount of time needed can be computed
    from the number of pages in the task. The tick() method decrements the
    internal timer and sets the printer to idle if the task is completed.

    Attributes:
        _page_rate (int/float) [10]: Number pages per minute a printer is
            capable.
        _current_task (_Task): Current _Task to be printed.
        _time_remaining (int/float): Remaining time of the current task to be
            finished.
    """

    def __init__(self, page_rate):
        self._page_rate = page_rate
        self._current_task = None
        self._time_remaining = 0

    def isBusy(self):
        return self._current_task is not None

    def tick(self):
        if self.isBusy():
            self._time_remaining -= 1
            # If the time required has reached 0, the printer is no longer busy.
            if self._time_remaining <= 0:
                self._current_task = None

    def startNext(self, new_task):
        self._current_task = new_task
        self._time_remaining = new_task.getPages() / self._page_rate * 60

    def timeRemaining(self):
        return self._time_remaining


class _Task(object):
    """Represent a single printing task.

    Attributes:
        _create_time: Time that the task was created and placed in the
            printer queue; used to compute waiting time.
    """

    def __init__(self, create_time):
        self._create_time = create_time
        self._pages = random.randrange(1, 20)  # Random int in range [1, 21).

    def getCreateTime(self):
        return self._create_time

    def getPages(self):
        return self._pages

    def waitTime(self, current_time):
        """The amount of time spent in the queue before printing begins."""
        return current_time - self._create_time


class Simulation(object):
    """Simulation of a lab with one printer and multiple users.

    Attributes:
        _printer (_Printer): A _Printer which can handle printing tasks.
        _task_queue (Queue): _Task instances wait to be processed.
        _waiting_times (list of int/float): Waiting time for each task.
    """

    def __init__(self, printer_page_rate=10, task_rate=20):
        """Initialize the printer and task queue.

        Args:
            printer_page_rate (int/float) [10]: Number pages per minute a
                printer is capable.
            task_rate (int/float) [20]: Number tasks per hour is generated.
        """
        self._printer = _Printer(printer_page_rate)
        self._task_queue = Queue()
        self._waiting_times = []
        self._task_rate = task_rate

    def run(self, num_seconds=3600):
        """Run the simulation.

        Args:
            num_seconds (int) [3600]: Total number of seconds to run the
                simulation.

        Raises:
            ValueError: if num_seconds is not valid.
        """
        if not isinstance(num_seconds, int) or num_seconds < 0:
            raise ValueError('num_seconds should be int < 0.')

        print('-' * 80)
        for current_second in xrange(num_seconds):
            # Does a new print task get created?
            if self._hasNew_Task():
                task = _Task(current_second)
                self._task_queue.enqueue(task)
                print('At %d sec: A task with %d pages occurs.' %
                      (current_second, task.getPages()))

            # If the printer is not busy and if >= 1 task is waiting.
            if not self._printer.isBusy() and not self._task_queue.isEmpty():
                next_task = self._task_queue.dequeue()
                self._waiting_times.append(next_task.waitTime(current_second))
                self._printer.startNext(next_task)
                print('At %d sec: The task created at %d sec is handled; needs '
                      '%d seconds to finish.' % (
                          current_second,
                          next_task.getCreateTime(),
                          self._printer.timeRemaining()))

            # The printer does one second of work if necessary.
            self._printer.tick()
        print('-' * 80)

    def statInfo(self):
        """Print statistic information of the simulation."""
        num_tasks = len(self._waiting_times)
        if num_tasks == 0:
            print('No task occurs.')
        else:
            average_waiting = sum(self._waiting_times) / num_tasks
            print('Average waiting %6.2f seconds %3d tasks remaining' %
                  (average_waiting, self._task_queue.size()))

    def _hasNew_Task(self):
        """Checks whether a new printing task has been created.

        The chance that at any given second, a print task is going to be
        created is 20 tasks/hour = 1/180 tasks/second. If the random number
        is 0, we say that a task has been created.
        """
        task_per_minute = self._task_rate / 3600
        return random.randrange(0, int(1 / task_per_minute)) == 0


def main():
    sim = Simulation()
    sim.run(3600)
    sim.statInfo()


if __name__ == '__main__':
    main()
