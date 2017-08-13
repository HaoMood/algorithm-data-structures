#!/usr/bin/env python
"""Use turtle to see recursion.

The turtle module is standard with all version of Python. You can create a
turtle and the turtle can move forward, backward, turn left. turn right, etc.
The turtle can have its tail up or down. When the turtle's tail is down and the
turtle moves it draws a line as it moves. You can also change the width of the
tail as well as the color of the ink the tail is dipped in.
"""

from __future__ import division, print_function

__all__ = ['Draw']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-27'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-27'
__version__ = '1.0'

import turtle


class Draw(object):
    """Use the turtle to draw shapes and figures.

    Attributes:
        turtle (Turtle)
        screen (Screen): A window for the turtle to draw in.
    """
    def __init__(self):
        self._turtle = turtle.Turtle()
        self._screen = turtle.Screen()

    def drawSpiral(self, line_length=200):
        """Use the turtle to draw a spiral recursively.

        Args:
            line_length (int >=0) [200]: Line length for the first stroke.

        Raises:
            ValueError: if line_length is not valid.
        """
        if not isinstance(line_length, int) or line_length < 0:
            raise('line_length should be int >= 0.')

        if line_length == 0:  # Base case
            return
        self._turtle.forward(line_length)
        self._turtle.right(90)
        self.drawSpiral(line_length - 5)  # Recursion with reduced length

    def drawFractalTree(self, branch_length=70):
        """Use the turtle to draw a fractal tree.

        The definition of a fractal is that when you look at in the fractal has
        the same basic shape no matter how much you magnify it.

        Args:
            branch_length (int >=0) [70]: Line length for the first tree.

        Raises:
            ValueError: if line_length is not valid.
        """
        if not isinstance(branch_length, int) or branch_length < 0:
            raise('branch_length should be int >= 0.')

        if branch_length <= 5:  # Base case
            return
        self._turtle.forward(branch_length)
        self._turtle.right(20)
        self.drawFractalTree(branch_length - 10)  # Recursion of the right tree.
        self._turtle.left(40)
        self.drawFractalTree(branch_length - 10)  # Recursion of the left tree.
        self._turtle.right(20)
        self._turtle.backward(branch_length)

    def drawTriangle(self, points):
        """Use the turtle to draw a triangle.

        Args:
            points (list of list of (int/float, int/float)): Three endpoints of
                a triangle.
        """
        self._turtle.up()
        self._turtle.goto(points[0][0], points[0][1])
        self._turtle.down()
        self._turtle.goto(points[1][0], points[1][1])
        self._turtle.goto(points[2][0], points[2][1])
        self._turtle.goto(points[0][0], points[0][1])

    def _getMid(self, point1, point2):
        return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2

    def drawSierpinskiTriangle(self, points, degree=7):
        """Use the turtle to draw a Sierpinski triangle.

        Start with a single large triangle. Divide the large triangle into four
        new triangles by connecting the midpoint of each side. Ignoring the
        middle triangle that you just created, apply the same procedure to each
        of the three corner triangles.

        Args:
            points (list of list of (int/float, int/float)): Three endpoints of
                the first triangle.
            degree (int) [3]: How many times do you want to divide the triangle
                into pieces
        """
        self.drawTriangle(points)
        if degree == 0:
            return
        mid01 = self._getMid(points[0], points[1])
        mid12 = self._getMid(points[1], points[2])
        mid02 = self._getMid(points[0], points[2])
        self.drawSierpinskiTriangle([points[0], mid01, mid02], degree - 1)
        self.drawSierpinskiTriangle([points[1], mid01, mid12], degree - 1)
        self.drawSierpinskiTriangle([points[2], mid02, mid12], degree - 1)

    def show(self):
        # Put the turtle into a wait mode until you click inside the window,
        # after which the program cleans up and exits.
        self._screen.exitonclick()


def main():
    """Use cases for the Draw class."""
    draw = Draw()
    #draw.drawSpiral()
    #draw.drawFractalTree()
    draw.drawSierpinskiTriangle([[-400, -200], [0, 400], [400, -200]])
    draw.show()


if __name__ == '__main__':
    main()
