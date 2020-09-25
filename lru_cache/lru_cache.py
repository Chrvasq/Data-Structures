import sys
sys.path.append('doubly_linked_list/')

from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage_dict = {}
        self.node_list = DoublyLinkedList()
        self.length = 0

    def __len__(self):
        return self.length
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.storage_dict:
            return None
        current_node = self.node_list.find_node_by_key(key)
        self.node_list.move_to_end(current_node)

        return self.storage_dict[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage_dict:
            # update node value
            self.node_list.update_node_value(key, value)
            # update storage dict value
            self.storage_dict[key] = value
        elif self.length is self.limit:  # if list is full
            # delete oldest and store removed key value pair
            deleted_node = self.node_list.remove_from_head()
            # remove key from storage dict
            self.storage_dict.pop(list(deleted_node.keys())[0])
            self.length -= 1

            # add new key value pair to tail
            self.node_list.add_to_tail({key: value})
            # add key value pair to storage dict
            self.storage_dict[key] = value
            self.length += 1
        else:
            self.node_list.add_to_tail({key: value})
            self.storage_dict[key] = value
            self.length += 1
