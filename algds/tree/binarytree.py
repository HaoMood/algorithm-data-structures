"""Implementation of a binary tree."""

from __future__ import division, print_function

__all__ = ['BinaryTree']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-28'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-28'
__version__ = '1.0'


class _Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insertLeft(self, key):
        if self.left is None:
            self.left = _Node(key)
        else:
            node = _Node(key)
            node.left = self.left
            self.left = node

    def insertRight(self, key):
        if self.right is None:
            self.right = _Node(key)
        else:
            node = _Node(key)
            node.right = self.right
            self.right = node


class BinaryTree(object):
    """ A binary tree with root node.

    >>> tree = BinaryTree('a')
    >>> print(tree.root.key)
    a
    >>> tree.root.insertLeft('b')
    >>> print(tree.root.left.key)
    b
    >>> tree.root.insertRight('c')
    >>> print(tree.root.right.key)
    c
    >>> tree.root.right.key = 'd'
    >>> print(tree.root.right.key)
    d
    >>> tree.root.insertLeft('e')
    >>> print(tree.root.left.key)
    e
    >>> print(tree.root.left.left.key)
    b
    """
    def __init__(self, key):
        self.root = _Node(key)

    def preorderTraversal(self):
        self._preorderTraversalHelper(self, self.root)

    def _preorderTraversalHelper(self, root):
        if root:
            print(root.key)
            self._preorderTraversalHelper(root.left)
            self._preorderTraversalHelper(root.right)

    def inorderTraversal(self):
        self._inorderTraversalHelper(self, self.root)

    def _inorderTraversalHelper(self, root):
        if root:
            self._inorderTraversalHelper(root.left)
            print(root.key)
            self._inorderTraversalHelper(root.right)

    def postorderTraversal(self):
        self._postorderTraversalHelper(self, self.root)

    def _postderTraversalHelper(self, root):
        if root:
            self._postorderTraversalHelper(root.left)
            self._postorderTraversalHelper(root.right)
            print(root.key)


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
