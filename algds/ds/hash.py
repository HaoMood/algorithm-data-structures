"""Implementation of hashing.

Searching in a hash table can take O(1) time.
"""

from __future__ import division, print_function

__all__ = ['HashTable']
__author__ = 'Hao Zhang'
__copyright__ = 'Copyright @2017'
__date__ = '2017-07-28'
__email__ = 'zhangh0214@gmail.com'
__license__ = 'CC BY-SA 3.0'
__status__ = 'Development'
__updated__ = '2017-07-28'
__version__ = '1.0'


class HashTable(object):
    """We create a hash table by using a list.

    The collisions are resolved by open addressing, to be more precise, linear
    probing.

    Attributes:
        _slots (list): Store the key-value pairs.

    >>> h = HashTable()
    >>> h[54] = 'cat'
    >>> h[26] = 'dog'
    >>> h[93] = 'lion'
    >>> h[17] = 'tiger'
    >>> h[77] = 'bird'
    >>> h[31] = 'cow'
    >>> h[44] = 'goat'
    >>> h[25] = 'pig'
    >>> h[20] = 'chicken'
    >>> print(h[20])
    chicken
    >>> print(h[17])
    tiger
    >>> h[20] = 'duck'
    >>> print(h[20])
    duck
    >>> print(h[99])
    None
    """
    def __init__(self, number_slots=11):
        self._slots = [[None, None] for _ in xrange(number_slots)]

    def _hash(self, key):
        """Copmute hash value for the key.

        When key is string, we use the folding method the compute the hash
        value. It begins by dividing the element into equal-size pieces (the
        last piece may not be of equal size). These pieces are then added
        together to give the resulting hash value, e.g., 4365554601 ->
        43 + 65 + 55 + 46 + 01 = 210, and then module the slot numbers.

        We can create hash functions for character-based items such as strings.
        The word "cat" can be thought of as a sequence of ordinal values:
        ord('c') == 99, ord('a') == 97, and ord('t') == 116. Note that anagrams
        will always be given the same hash value.

        Args:
            key (str/int)

        Raises:
            ValueError: If the key type is not valid.
        """
        if isinstance(key, str):
            # TODO (Hao): Use the position of the character as a weight.
            return sum([ord(ch) for ch in key]) % len(self._slots)
        if isinstance(key, int):
            return key % len(self._slots)
        else:
            raise ValueError('key type should be str/int.')

    def __setitem__(self, key, val):
        """Add a new key-value pair to the hash table.

        If the key is already in the map, then replace the old value with the
        new one.

        Args:
            key (int/str)
            val

        Raises:
            RuntimeError: If the slots are out of storage.
        """
        hash_value = self._hash(key)
        new_hash_value = None
        for i in xrange(len(self._slots)):
            new_hash_value = (hash_value + i) % len(self._slots)
            if self._slots[new_hash_value][0] is None:
                # The slot is not used.
                self._slots[new_hash_value][0] = key
                self._slots[new_hash_value][1] = val
                return
            if self._slots[new_hash_value][0] == key:
                # Replace the old value.
                self._slots[new_hash_value][1] = val
                return
        raise RuntimeError('Out of storage of the slots.')

    def __getitem__(self, key):
        """Given a key.

        Return the value stored in the hash table or None otherwise.

        Args:
            key (int/str)
        """
        hash_value = self._hash(key)
        new_hash_value = None
        for i in xrange(len(self._slots)):
            new_hash_value = (hash_value + i) % len(self._slots)
            if self._slots[new_hash_value][0] is None:
                return None
            if self._slots[new_hash_value][0] == key:
                return self._slots[new_hash_value][1]
        return None

    def __delitem__(self, key):
        """Delete the key-value pair from the hash table using 'del h[key]'."""
        # TODO (Hao): Implement this method.
        raise NotImplementedError

    def __contains__(self, key):
        """For the statement 'key in d'."""
        # TODO (Hao): Implement this method.
        raise NotImplementedError


def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test()
