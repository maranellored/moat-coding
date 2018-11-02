################################################################################
##
##  A basic hashmap class.
##  Uses an internal class to store the items
##
##  ** This class does not protect against concurrency **
##
##  The class uses a list to store all the buckets internally.
##  Each bucket is in turn another list of the items that are stored in the
##  hashmap.
##
##  The time taken to look up each bucket is constant. A bucket for an item is
##  chosen by hashing the key for the item using the python hash function.
##  Then the bucket is simply the hash modulo the size of the list.
##  A bucket can have multiple items hashing to it. This is handled by the
##  internal list for the bucket.
##
##  The initial size of the hashmap is initialized to 32.
##  The load factor is 0.75. If the number of items in the hashmap exceed
##  load_factor * size, then the items are rehashed, after doubling the size
##  of the internal list. This load check and the rehash operation are performed
##  during the the add operation.
##
##  The hashmap class provides the following methods
##  - Add()
##      Adds the specified key and value to the hashmap. If an object already
##      exists with the given key, then it is replaced.
##  - Remove()
##      Removes the item that is identified by the given key.
##      If no item exists with the specified key, then a KeyError is raised.
##      Returns the value of the item that was removed.
##  - Get()
##      Returns the value for the item that is identified by the given key.
##      If no item exists with the specified key, then a KeyError is raised.
##  - Size()
##      Returns the count of items that exist in the hashmap.
##  - Items()
##      Returns a list of tuples of all the key-value pairs that have been
##      stored in this hashmap.
##  - Keys()
##      Returns a list of all the keys of items that exist in the hashmap
##  - Values()
##      Returns a list of all the values of items that exist in the hashmap.
##  - IterKeys()
##      Provides a generator that can be used to iterate over the keys of the
##      hashmap. Useful if you dont need to create a copy of the keys.
##  - IterValues()
##      Provides a generator that can be used to iterate over the value of the
##      items in thehashmap. Useful if you dont need to create a copy of the
##      keys.
##  - IterItems()
##      Provides a generator that can be used to iterate over the items in the
##      hashmap. Returns a tuple containing the key-value pair
##
################################################################################


class __Item__(object):
    """
    A private class that is used by the hashmap class to keep track of items
    that are added to the hashmap.
    Only contains two fields that are initialized upon object creation, and
    the fields are retrievable via the getter methods.
    """
    def __init__(self, key, value):
        self._key = key
        self._value = value

    def get_key(self):
        return self._key

    def get_value(self):
        return self._value


class HashMap(object):
    """
    The actual hashmap class
    Maintains a list internally to keep track of items.
    """
    _DEFAULT_INITIAL_SIZE = 32

    # The default load factor is randomly chosen. No benchmarks.
    # This was inspired by the Java standard lib implementation of hashmap
    # which uses 0.75 and considers it as an optimal value for performance
    _LOAD_FACTOR = 0.75

    def __init__(self, capacity=_DEFAULT_INITIAL_SIZE):
        self._size = 0

        if capacity < 0:
            capacity = HashMap._DEFAULT_INITIAL_SIZE
        self._capacity = capacity
        # Initialize every bucket to None at start
        self._list = [None] * capacity

    def add(self, key, value):
        index = self._get_index(key)
        item = __Item__(key, value)

        self._add_internal(item, index)
        self._size += 1
        if self._size > (self._capacity * HashMap._LOAD_FACTOR):
            self._rehash()

    def get(self, key):
        index = self._get_index(key)

        bucket = self._list[index]
        if bucket is None:
            raise KeyError("The specified key doesn't exist in the hashmap")

        for i in bucket:
            if i.get_key() == key:
                return i.get_value()

        raise KeyError("The specified key doesn't exist in the hashmap")

    def remove(self, key):
        index = self._get_index(key)

        bucket = self._list[index]
        if bucket is None:
            raise KeyError("The specified key doesn't exist in the hashmap")

        item = self._remove_internal(key, bucket)
        if item is None:
            raise KeyError("The specified key doesn't exist in the hashmap")

        self._size -= 1
        return item.get_value()

    def size(self):
        return self._size

    def items(self):
        """
        Returns a list of all key value pairs that exist in the hashmap.
        This method returns a list of tuples where the first element of the
        tuple is the key and the second element is the value
        The list is a copy of the items from the hashmap
        """
        items = []
        for item in self._item_iterator():
            tup = (item.get_key(), item.get_value())
            items.append(tup)

        return items

    def keys(self):
        """
        Returns a list of all keys for all items that exist in the hashmap.
        The list is a copy of the keys from the hashmap
        """
        keys = []
        for item in self._item_iterator():
            keys.append(item.get_key())

        return keys

    def values(self):
        """
        Returns a list of all values for the items that exist in the hashmap
        The list is a copy of the values from the hashmap
        """
        values = []
        for item in self._item_iterator():
            values.append(item.get_value())

        return values

    def itervalues(self):
        """
        Returns an iterator over the values in the hashmap.
        It does not create a new list
        """
        for item in self._item_iterator():
            yield item.get_value()

    def iterkeys(self):
        """
        Returns an iterator over the keys in the hashmap
        It does not create a new list
        """
        for item in self._item_iterator():
            yield item.get_key()

    def iteritems(self):
        """
        Returns an iterator over the keys in the hashmap
        It does not create a new list
        """
        for item in self._item_iterator():
            yield (item.get_key(), item.get_value())

    # Everything under here are private methods used internally by the class
    def _get_index(self, key):
        """
        Simplistic hash funGction that returns the hash for a given key.
        Uses the built in python hash function.
        """
        hash_value = hash(key)
        index = hash_value % self._capacity

        return index

    def _rehash(self):
        # increase the capacity of the list by twice the current
        # capacity
        self._capacity *= 2
        new_list = [None] * (self._capacity)

        old_list = self._list
        self._list = new_list
        # rehash the old list.
        for bucket in old_list:
            if bucket is None:
                continue

            for item in bucket:
                index = self._get_index(item.get_key())
                self._add_internal(item, index)

    def _add_internal(self, item, index):
        bucket = self._list[index]

        if bucket is None:
            self._list[index] = [item]
            return

        # we need to remove the key if it already exists in our
        # internal list
        self._remove_internal(item.get_key(), bucket)

        bucket.append(item)

    def _remove_internal(self, key, bucket):
        """
        This method helps remove the given key from the list represented
        by bucket.
        If the key doesnt exist in the bucket, then it leaves the bucket
        unchanged.
        This method does change the list in place. This method is OK in this
        case since we dont iterate further after we remove the item from the
        list. If we were to iterate further, then this pattern could skip
        elements in the list
        """
        for idx, item in enumerate(bucket):
            if item.get_key() == key:
                return bucket.pop(idx)

        return None

    def _item_iterator(self):
        """
        A generator that iterates over the items that are stored in the
        hashmap.
        """
        for bucket in self._list:
            if bucket is None:
                continue

            for item in bucket:
                yield item
