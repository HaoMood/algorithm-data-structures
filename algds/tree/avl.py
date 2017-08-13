"""Implementation of an AVL tree.

An AVL tree implements the map ADT just like a regular binary search tree, the
only difference is in how the tree performs. To implement ur AVL tree we need
to keep track of a balance factor for each node in the tree:
    balance_factor := left_subtree_height - right_subtree_height .
We will define a tree to be balance if the balance factor is -1, 0, 1. Once the
balance factor of a node in a tree is outside this range we will need to have
a procedure to bring the tree back into balance.
"""

from __future__ import division, print_function

__all__ = ['AVL']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-08-13'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-08-13'
__version__ = '1.0'

from bst import _Node, BST


class AVL(BST):
    """Implementation of an AVL tree.
    """
    def _setItemHelper(self, key, value, node):
        if key < node.key:
            if node.hasLeft():
                self._setItemHelper(key, value, node.left)
            else:
                node.left = _Node(key, value, parent=node)
                self._updateBalance(node.left)   # Addition code
        else:
            if node.hasRight():
                self._setItemHelper(key, value, node.right)
            else:
                node.right = _Node(key, value, parent=node)
                self._updateBalance(node.right)  # Addition code

    def _updateBalance(self, node):
        # Check if the current node is out of balance.
        if node.balance_factor > 1 or node.balance_factor < -1:
            self._rebalance(node)
            return
        # If the current node does not require rebalancing then the balance
        # factor of the parent is adjusted.
        if node.parent != None:
            if node.isLeft():
                node.parent.balance_factor += 1
            if node.isRight():
                node.parent.balance_factor -= 1
            if node.parent.balance_factor != 0:
                # If the balance factor is non-zero, then the algorithm
                # continues to work its way up the tree toward the root.
                self._updateBalance(node.parent)

    def rotateLeft(self, root):
        pass

    def _rebalance(self, node):
        pass


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
