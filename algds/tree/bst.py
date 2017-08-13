"""The implementation of a binary search tree.
"""

from __future__ import division, print_function

__all__ = ['BST']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-08-12'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-08-12'
__version__ = '1.0'


class _Node(object):
    """Provide many helper functions that make the work doen in the BST class
    methods much easier.

    These helper functions help to classify a node according to its own position
    as a child, (left or right) and the kind of children the node has. This
    class will also explicitly keep track of the parent as an attribute of each
    node.
    """
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def hasLeft(self):
        return self.left

    def hasRight(self):
        return self.right

    def isLeft(self):
        return self.parent and self.parent.left == self

    def isRight(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not self.left and not self.right

    def hasAnyChildren(self):
        return self.left or self.right

    def hasBothchildren(self):
        return self.left and self.right

    def replaceNodeData(self, key, value, left_child, right_child):
        self.key = key
        self.value = value
        self.left = left_child
        self.right = right_child
        if self.hasLeft():
            self.left.parent = self
        if self.hasRight():
            self.right.parent = self

    def __iter__(self):
        if self:
            if self.hasLeft():
                for element in self.left():
                    yield element
            yield self.key
            if self.hasRight():
                for element in self.right():
                    yield element

    def findSuccessor(self):
        if self.hasRight():
            # If the node has a right child, then the successor is the smallest
            # key in the right subtree.
            successor = self.right.findMin()
        elif self.parent:
            if self.isLeft():
                # If the node has no right child and is the left child of
                # its parent, then the parent is the successor.
                successor = self.parent
            else:
                # If the node is the right child of its parent, and itself
                # has no right child, then the successor to this node is the
                # successor of its parent, excluding this node.
                self.parent.right = None
                successor = self.parent.findSuccessor()
                self.parent.right = self
        else:
            successor = None
        return successor

    def findMin(self):
        current = self
        # Follow the left references in each node of the subtree until it
        # reaches a node that does not have a left child.
        while current.hasLeft():
            current = current.left
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeft():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.hasLeft():
                if self.isLeft():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isLeft():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent


class BST(object):
    """Implementation of a binary search tree.

    >>> bst = BST()
    >>> bst[3] = 'red'
    >>> bst[4] = 'blue'
    >>> bst[6] = 'yellow'
    >>> bst[2] = 'at'
    >>> print(bst[6])
    yellow
    >>> print(bst[2])
    at
    """
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        return self._root.__iter__()

    def __setitem__(self, key, value):
        """Overload the [] operator for assignment by having the __setitem__
        method call.

        This allow us to write Python statements like bst['Plymouth'] = 55446.
        """
        if self._root:
            self._setItemHelper(key, value, self._root)
        else:
            self._root = _Node(key, value)
        self._size += 1

    def _setItemHelper(self, key, value, node):
        if key < node.key:
            if node.hasLeft():
                self._setItemHelper(key, value, node.left)
            else:
                node.left = _Node(key, value, parent=node)
        else:
            if node.hasRight():
                self._setItemHelper(key, value, node.right)
            else:
                node.right = _Node(key, value, parent=node)

    def __getitem__(self, key):
        """It uses the same logic for choosing the left and right child as the
        __setitem__ method.

        By overloading [], we can write a Python statement that looks just like
        we are accessing a dictionary: z = bst['Fargo'].
        """
        if self._root:
            node = self._getItemHelper(key, self._root)
            if node:
                return node.value
            else:
                return None
        else:
            return None

    def _getItemHelper(self, key, node):
        if not node:
            return None
        elif node.key == key:
            return node
        elif node.key < key:
            return self._getItemHelper(key, node.left)
        else:
            return self._getItemHelper(key, node.right)

    def __contains__(self, key):
        """Implement the in operator."""
        return self.__getitem__(key)

    def __delitem__(self, key):
        """Delete the node by searching the tree.
        """
        if self._size > 1:
            node_to_delete = self._getItemHelper(key, self._root)
            if node_to_delete:
                self._delItemHelper(node_to_delete)
                self._size -= 1
            else:
                raise KeyError('Key is not in the tree.')
        elif self._size == 1 and self._root.key == key:
            self._root = None
            self._size -= 1
        else:
            raise KeyError('Key is not in the tree.')

    def _delItemHelper(self, node):
        if node.isLeaf():  # If the node to be deleted has no children
            if node.isLeft():
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.hasBothchildren():  # If the node has both children
            successor = node.findSuccessor()
            successor.spliceOut()
            node.key = successor.key
            node.value = successor.value
        else:
            if node.hasLeft():  # If the node has only one children
                if node.isLeft():
                    # If the current node is a left child then we only need to
                    # update the parent reference of the left child to point to
                    # the parent of the current node, and then update the left
                    # child reference of the parent to point to the current
                    # node's left child.
                    node.left.parent = node.parent
                    node.parent.left = node.left
                elif node.isRight():
                    # If the current node is a right child then we only need
                    # to update the parent reference of the left child to
                    # point to the parent of the current node, and then
                    # update the right child reference of the parent to point
                    # to the current node's right child.
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:
                    # If the current node has no parent (i.e., it is the
                    # root). We replace the key, value, left_child,
                    # right_child data by calling replaceNodeData method on
                    # the root.
                    node.replaceNodeData(node.left.key, node.left.value,
                                         node.left.left, node.left.right)
            else:
                # The cases are symmetric wrt either having a left or right
                # child.
                if node.isLeft():
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.isRight():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    node.replaceNodeData(node.right.key, node.right.value,
                                         node.right.left, node.right.right)



def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
