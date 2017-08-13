#!/usr/bin/env python
"""Exploring a Maze.

Suppose the maze is divided up into squares. Each square of the maze is either
open or occupied by a section of wall. The turtle can only pass through the open
squares of the maze.

We should have a strategy to remember where we have been. In this case we will
assume that we have a bag of bread crumbs we can drop along the way. If we take
a step in a certain direction and find there is a bread crumb already on that
square, we know that we should immediately back up and try the next direction
in our procedure.
"""

from __future__ import division, print_function

__all__ = ['Maze']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-27'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-27'
__version__ = '2.0'  # Refactor the code.

import turtle


class Maze(object):
    """Representation of a Maze.

    Attributes:
        TYPE (dict of (str, str)): Valid types in a maze map.
        start_row (int): Starting point's row coordinate.
        start_col (int): Starting point's column coordinate.

        _maze_map (list of list of str): Map of the maze. We use '#' to
            represent walls, ' ' to represent open squares, and 'S' to indicate
            the starting position.
        _num_rows (int): Total number of rows.
        _num_cols (int): Total number of columns.
        _turtle (Turtle)
        _screen (Screen)
        _row_translate (int/float): Row offset for drawing on the screen.
        _col_translate (int/float): Column offset for drawing on the screen.
    """

    TYPE = {'obstacle': '#', 'tried': '.', 'part_of_path': '@', 'dead_end': 'x'}
    COLOR = {'obstacle': 'black', 'tried': 'green', 'part_of_path': 'blue',
             'dead_end': 'red'}

    def __init__(self, file_name):
        """Read from a data file representing a maze and initialize.

        Initialize the internal representation of the maze, and finds the
        starting position for the turtle. Setup the GUI.

        Args:
            file_name (str): The name of the maze file. This is a text file
                using the same format as _maze_map attribute.

        Raises:
            ValueError: If the input file is invalid.
        """
        self._maze_map = []
        self.start_row = None
        self.start_col = None
        with open(file_name, 'r') as f:
            for i, line in enumerate(f.readlines()):
                line = line.strip('\n')
                self._maze_map.append(list(line))
                j = line.find('S')
                if j != -1:  # If found
                    self.start_row = i
                    self.start_col = j
        if self.start_row is None or self.start_col is None:
            raise ValueError('Input file has not starting point.')
        self._num_rows = len(self._maze_map)
        self._num_cols = len(self._maze_map[0])

        self._turtle = turtle.Turtle()
        self._turtle.shape('turtle')
        self._screen = turtle.Screen()
        # turtle.setworldcoordinates(llx, lly, urx, ury)
        # Set up user-defined coordinate system.
        # llx: Horizontal coordinate of lower left corner of canvas.
        # lly: Vertical coordinate of lower left corner of canvas.
        # urx: Horizontal coordinate of upper right corner of canvas.
        # ury: Vertical coordinate of upper right corner of canvas.
        self._screen.setworldcoordinates(
            -(self._num_cols - 1) / 2 - 0.5, -(self._num_rows - 1) / 2 - 0.5,
            (self._num_cols - 1) / 2 + 0.5, (self._num_rows - 1) / 2 + 0.5)
        self._row_translate = self._num_rows / 2
        self._col_translate = -self._num_cols / 2

    def holdOn(self):
        """Hold on the screen until we click."""
        self._screen.exitonclick()

    def successFrom(self, row, col):
        """Checks whether we can succeed if we start at row and start col.

        Args:
            row (int): Starting point's row coordinate.
            col (int): Starting point's column coordinate.

        Returns:
            bool: True if we succeed in find a path from row, col.
        """
        # Check the first three of the four base cases.
        # 1. We have run into an obstacle (wall). Since the square is occupied
        #    by a wall no further exploration can take place.
        # 2. We have found a square that has already been explored. We do not
        #    want to continue exploring from this position or we will get a
        #    loop.
        if (self._maze_map[row][col] == self.TYPE['obstacle'] or
            self._maze_map[row][col] == self.TYPE['tried'] or
            self._maze_map[row][col] == self.TYPE['dead_end']):
            return False

        # 3. We have found an outside edge, not occupied by a wall. In other
        #    words we have found an exit from the maze.
        if self._hasExit(row, col):
            self._mark(row, col, 'part_of_path')
            return True

        # Otherwise, use logical short circuiting to try each direction in turn
        # if needed.
        self._mark(row, col, 'tried')
        if (self.successFrom(row - 1, col) or
            self.successFrom(row + 1, col) or
            self.successFrom(row, col - 1) or
            self.successFrom(row, col + 1)):
            self._mark(row, col, 'part_of_path')
            return True
        else:
            # 4. We have explored a square unsuccessfully in all four
            #    directions.
            self._mark(row, col, 'dead_end')
            return False

    def _mark(self, row, col, val):
        """Set the row, col position of the map according val, and move to that
        position.

        Args:
            row (int): The current positions's row coordinate.
            col (int): The current positions's column coordinate.
        """
        self._maze_map[row][col] = self.TYPE[val]
        self._moveTurtle(row, col)
        self._turtle.dot(10, self.COLOR[val])  # Drop a bread crumb.

    def _hasExit(self, x, y):
        """Check to see if the current position is an exit from the maze.

        An exit condition is whenever the turtle has navigated to the edge of
        the maze, either row zero or column zero, or the far right column or
        the bottom row.

        Args:
            row (int): The current positions's row coordinate.
            col (int): The current positions's column coordinate.

        Returns:
            bool: True if we have exited now.
        """
        return (x == 0 or x == self._num_rows - 1 or
                y == 0 or y == self._num_cols - 1)

    def _moveTurtle(self, row, col):
        """Move the turtle to the row, col position.

        It helps you visualize the algorithm so that you can watch exactly how
        the turtle explores its way through the maze.

        Args:
            row (int): The desired positions's row coordinate.
            col (int): The desired positions's column coordinate.
        """
        self._turtle.up()
        self._turtle.setheading(self._turtle.towards(
            col + self._col_translate, -row + self._row_translate))
        self._turtle.goto(col + self._col_translate, -row + self._row_translate)

    def drawMaze(self):
        """Draw the maze in a window on the screen."""
        self._turtle.speed(10)
        self._screen.tracer(0)  # Turn animation off
        for i in xrange(self._num_rows):
            for j in xrange(self._num_cols):
                if self._maze_map[i][j] == self.TYPE['obstacle']:
                    self._drawCenteredBox(
                        j + self._col_translate, -i + self._row_translate,
                        'orange')
        self._turtle.color('black')
        self._turtle.fillcolor('blue')
        self._screen.update()   # Perform update; used when tracer is off.
        self._screen.tracer(1)  # Turn animation on

    def _drawCenteredBox(self, hori, vert, color):
        """Draw a box centered at hori, vert."""
        self._turtle.up()
        self._turtle.goto(hori - 0.5, vert - 0.5)
        self._turtle.color(color)
        self._turtle.fillcolor(color)
        self._turtle.setheading(90)  # Orientation to the north.
        self._turtle.down()
        self._turtle.begin_fill()
        for _ in xrange(4):
            self._turtle.forward(1)
            self._turtle.right(90)
        self._turtle.end_fill()

    def __str__(self):
        """Display the maze map in the terminal."""
        str_output = []
        for i in xrange(self._num_rows):
            str_output.append(''.join(self._maze_map[i]))
        return '\n'.join(str_output)

    __repr__ = __str__


def main():
    maze = Maze('./maze_map.dat')
    maze.drawMaze()
    maze.successFrom(maze.start_row, maze.start_col)
    maze.holdOn()


if __name__ == '__main__':
    main()
