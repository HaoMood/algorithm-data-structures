"""Implementation of a parse tree.

Parse trees can be used to represent real-world constructions like sentences
or mathematical expressions. The hierarchy of the tree helps us understand
the order of evaluation for the whole expression.
"""

from __future__ import division, print_function

__all__ = ['ParseTree']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-28'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-08-12'
__version__ = '1.0'

import operator
import sys
sys.path.append('../../')

from algds.ds.stack import Stack
from algds.tree.binarytree import BinaryTree


class ParseTree(object):
    """Implementation of a parse tree.

    We need to build a parse tree from a fully parenthesized mathematical
    expression, evaluate the expression stored in the parse tree, and recover
    the original expression from the parse tree.

    Whenever we read a left parenthesis we are starting a new expression,
    and hence we should create a new tree to correspond to that expression.
    Conversely, whenever we read a right parenthesis, we have finished an
    expression.

    We also know that the operands are going to be the leaf nodes and children
    of their operators. Besides, every operator is going to have a left and
    a right child.

    >>> parse_tree = ParseTree('( ( 10 + 5 ) * 3 )')
    >>> parse_tree.evaluate()
    45
    >>> parse_tree.recover()
    '( ( 10 + 5 ) * 3 )'
    >>> parse_tree = ParseTree('( 3 + ( 4 * 5 ) )')
    >>> parse_tree.evaluate()
    23
    >>> parse_tree.recover()
    '( 3 + ( 4 * 5 ) )'
    """
    def __init__(self, expression):
        """Build a parse tree from a fully parenthesized mathematical
        expression.
        """
        # We need to keep track of the current node as well as the parent of the
        # current node. We will use a stack to keep track of parents. Whenever
        # we want to descend to a child of the current node, we first push the
        # current node on the stack. When we want to return to the parent of the
        # current node, we pop the parent off the stack.
        stack = Stack()
        self._tree = BinaryTree('')
        stack.push(self._tree)
        current_tree = self._tree.root
        for ch in expression.split():  # For each token in the expression string
            if ch == '(':
                # Start a new expression, and hence we create a new tree to
                # correspond to that expression. We need to add a new node as
                # the left child of the current node and descend to the left
                # child.
                current_tree.insertLeft('')
                stack.push(current_tree)
                current_tree = current_tree.left
            elif ch in ')':
                # Finish that expression. Go to the parent of the current node.
                current_tree = stack.pop()
            elif ch in '+-*/':
                # Every operator is going to have both a left and a right child.
                # We set the root value of the current node to the operator.
                current_tree.key = ch
                current_tree.insertRight('')
                stack.push(current_tree)
                current_tree = current_tree.right
            else:  # ch is an operand
                # Operands are going to be leaf nodes and children of their
                # operators. We set the root value of the current node to the
                # number and return to the parent.
                current_tree.key = int(ch)
                current_tree = stack.pop()

    def evaluate(self):
        """Evaluate the expression stored in a parse tree."""
        return self._evaluateHelper(self._tree.root)

    def _evaluateHelper(self, root):
        # We can evaluate a parse tree be recursively evaluating each subtree.
        operators = {'+': operator.add, '-': operator.sub,
                     '*': operator.mul, '/': operator.div}

        left_child = root.left
        right_child = root.right

        if left_child and right_child:
            function = operators[root.key]
            return function(self._evaluateHelper(left_child),
                            self._evaluateHelper(right_child))
        else:
            # Base case: leaf node. In a parse tree, the leaf nodes will always
            # be operands. We can simply return the value stored in the leaf
            # node.
            return root.key

    def recover(self):
        """Recover the original mathematical expression from a parse tree.

        It is a inorder tree walk. The only modifications we will make are
        printing parentheses before and after the subtree call.
        """
        return self._recoverHelper(self._tree.root)

    def _recoverHelper(self, root):
        expression = []
        if root.left and root.right:
            expression.append('(')
            expression.append(self._recoverHelper(root.left))
            expression.append(str(root.key))
            expression.append(self._recoverHelper(root.right))
            expression.append(')')
        else:
            expression.append(str(root.key))
        return ' '.join(expression)


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
