"""Sorting."""

from __future__ import division, print_function

__all__ = ['bubbleSort', 'selectionSort', 'insertionSort', 'shellSort',
           'mergeSort', 'quickSort']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017 LAMDA'
__date__ = '2017-07-28'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-28'
__version__ = '1.0'


def bubbleSort(A):
    """The bubble sort compares adjacent items and exchanges those that are out
    of order.

    Each pass through the list places the next largest value in its proper
    place. In essence, each item "bubbles" up to the location where it belongs.

    The bubble sort is often considered the most inefficient sorting method
    since it must exchange items before the final location is known. These
    "wasted" exchange operations are very costly.

    On the other hand, if during a pass there are no exchanges, then we know
    that the list must be sorted. A bubble sort can be modified to stop early
    if it finds the list has become sorted.

    >>> bubbleSort([])
    []
    >>> bubbleSort([1])
    [1]
    >>> bubbleSort([1, 2])
    [1, 2]
    >>> bubbleSort([2, 1])
    [1, 2]
    >>> bubbleSort([2, 1, 3])
    [1, 2, 3]
    >>> bubbleSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    n = len(A)
    for i in xrange(n - 1, 0, -1):
        is_sorted = True
        for j in xrange(i):
            if A[j] > A[j + 1]:
                is_sorted = False
                A[j], A[j + 1] = A[j + 1], A[j]
        if is_sorted:
            break
    return A


def selectionSort(A):
    """The selection sort improves on the bubble sort by making only one
    exchange for every pass through the list.

    In order to do this, a selection sort looks for the largest value as it
    makes a pass and, after completing the pass, places it in the proper
    location. As with a bubble sort, after the first pass, the largest item
    is in the correct place. This process continues and requires n-1 passes
    to sort n items, since the final item must be in place after the (n-1)-th
    pass.

    >>> selectionSort([])
    []
    >>> selectionSort([1])
    [1]
    >>> selectionSort([1, 2])
    [1, 2]
    >>> selectionSort([2, 1])
    [1, 2]
    >>> selectionSort([2, 1, 3])
    [1, 2, 3]
    >>> selectionSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    n = len(A)
    for i in xrange(n - 1, 0, -1):
        max_index = 0
        for j in xrange(1, i + 1):
            if A[j] > A[max_index]:
                max_index = j
        A[max_index], A[i] = A[i], A[max_index]
    return A


def insertionSort(A):
    """Insertion sort always maintains a sorted sublist in the lower positions
    of the list.

    Each new element is then "inserted" back into the previous sublist such that
    the sorted sublist is one item larger.

    >>> insertionSort([])
    []
    >>> insertionSort([1])
    [1]
    >>> insertionSort([1, 2])
    [1, 2]
    >>> insertionSort([2, 1])
    [1, 2]
    >>> insertionSort([2, 1, 3])
    [1, 2, 3]
    >>> insertionSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    n = len(A)
    for i in xrange(1, n):
        current_value = A[i]
        j = i - 1
        while j >= 0 and A[j] > current_value:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = current_value
    return A


def shellSort(A):
    """Perform shell sort on list A.

    The shell sort, sometimes called the diminishing increment sort, improves
    on the insertion sort by breaking the original list into a number of smaller
    sublists, each of which is sorted using an insertion sort.

    The unique way that these sublists are chosen is the key to the shell sort.
    Instead of breaking the list into sublists of contiguous items, the shell
    sort uses an increment i, sometimes called the gap, to create a sublist
    by chosing all items that are i items apart.

    By sorting the sublists, although the whole list is not completely sorted,
    the elements are closer to where they actually belong. We perform a final
    insertion sort by using an increment of one, i.e., the standard insertion
    sort. Note that by performing the earlier sublist sorts, we have now reduced
    the total number of shifting operations necessary to put the list in its
    final order.

    Since each pass produces a list that is "more sorted" than the previous
    one, the final insertion sort does not need to do very many comparisons.
    The running time of a shell sort is between O(n) and O(n^2). By changing the
    increment, for exmample using 2^k-1 (1, 3, 7, 15, 31, ...), a shell sort
    can perform at O(n^(3/2)).

    >>> shellSort([])
    []
    >>> shellSort([1])
    [1]
    >>> shellSort([1, 2])
    [1, 2]
    >>> shellSort([2, 1])
    [1, 2]
    >>> shellSort([2, 1, 3])
    [1, 2, 3]
    >>> shellSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    n = len(A)
    gap = n // 2
    while gap > 0:
        for start in xrange(gap):
            _gapInsertionSort(A, start, gap)
        gap //= 2
    return A


def _gapInsertionSort(A, start, gap):
    """Helper function of shellSort()."""
    n = len(A)
    for i in xrange(start + gap, n, gap):
        current_value = A[i]
        j = i - gap
        while j >= start and A[j] > current_value:
            A[j + gap] = A[j]
            j -= gap
        A[j + gap] = current_value
    return A


def mergeSort(A):
    """Mergesort uses a divide and conquer strategy to improve the performance.

    Merge sort is a recursive algorithm that continually splits a list in half,
    and recursive invoke a merge sort on both halves.

    >>> mergeSort([])
    []
    >>> mergeSort([1])
    [1]
    >>> mergeSort([1, 2])
    [1, 2]
    >>> mergeSort([2, 1])
    [1, 2]
    >>> mergeSort([2, 1, 3])
    [1, 2, 3]
    >>> mergeSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    n = len(A)
    if n <= 1:
        return A

    mid = n // 2
    A1 = mergeSort(A[:mid])
    A2 = mergeSort(A[mid:])
    return _merge(A1, A2)


def _merge(A1, A2):
    """Helper function for mergeSort().

    Merging is the process of taking two smaller sorted list and combining
    them together into a single, sorted, new list.
    """
    n1 = len(A1)
    n2 = len(A2)
    A = []

    i = 0
    j = 0
    while i < n1 and j < n2:
        if A1[i] <= A2[j]:
            A.append(A1[i])
            i += 1
        else:
            A.append(A2[j])
            j += 1

    if i != n1:
        A.extend(A1[i:])
    if j != n2:
        A.extend(A2[j:])
    return A


def quickSort(A):
    """The quick sort uses divide and conquer to gain the same advantages as the
    merge sort, while not using additional storage.

    As a trade-off, however, it is possible that the list may not be divided in
    half. We use the first item in the list to be the pivot.

    >>> quickSort([])
    []
    >>> quickSort([1])
    [1]
    >>> quickSort([1, 2])
    [1, 2]
    >>> quickSort([2, 1])
    [1, 2]
    >>> quickSort([2, 1, 3])
    [1, 2, 3]
    >>> quickSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    _quickSortHelper(A, 0, len(A) - 1)
    return A


def _quickSortHelper(A, p, r):
    if p < r:
        q = _partition(A, p, r)
        _quickSortHelper(A, p, q - 1)
        _quickSortHelper(A, q + 1, r)


def _partition(A, p, r):
    """Partite the array around the pivot."""
    pivot = A[p]
    left_mark = p + 1
    right_mark = r

    while True:
        # Increment left_mark until we locate a value that is > pivot.
        while left_mark <= right_mark and A[left_mark] <= pivot:
            left_mark += 1
        # Decrement right_mark until we locate a value that is < pivot.
        while left_mark <= right_mark and A[right_mark] >= pivot:
            right_mark -= 1
        # At this point, we discover two items that are out of place.
        if left_mark < right_mark:
            A[left_mark], A[right_mark] = A[right_mark], A[left_mark]
        else:
            break

    A[p], A[right_mark] = A[right_mark], A[p]
    return right_mark


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
