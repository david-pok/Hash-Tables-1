# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
    # # Start from an arbitrary large prime
    # hash_value = 5381
    # # Bit-shift and sum value for each character
    # for char in key:
    #     hash_value = ((hash_value << 5) + hash_value) + char
    # return hash_value
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # use hash_mod to get the correct index of the key
        # create a LinkedPair thing using the given key, value
        # insert the new LinkedPair thing into the calculated index of storage
        # if there is something there, set the newly inserted as the next to already inserted
        index = self._hash_mod(key)
        inserting = LinkedPair(key, value)
        node = self.storage[index]
        final_node = None

        while node is not None and node.key != key:
            final_node = node
            node = final_node.next

        if node is None:
            inserting.next = self.storage[index]
            self.storage[index] = inserting
        else:
            node.value = value

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass
        # use hash_mod to calculate index from the key
        # if the index has nothing, print the warning
        # if the first linkedPair has the key we remove it
        # if it doesn't, look at the linkedPair's next's key
        # repeat if necesary
        # remove if found
        index = self._hash_mod(key)
        node = self.storage[index]
        cur_node = None
        prev_node = None

        while node.key != key:
            prev_node = node
            node = prev_node.next

        if node is None:
            print("Not Found")

        else:
            if prev_node is None:
                self.storage[index] = node.next
            else:
                prev_node.next = node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        pass
        # hash_mod to calculate index
        # look into index, if none, then return none
        # if there is, match key, if matched, return value
        #if no match, check the next, repeat if necesary
        # return value
        index = self._hash_mod(key)
        node = self.storage[index]
        next_node = None

        if node is None:
            return None

        while node is not None:
            if node.key == key:
                return node.value

            next_node = node.next
            node = next_node

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        #save copy of old storage in variable
        #double capacity/storage
        #iterate through and copy old storage into new storage
        #point storage to new storage
        old_capacity = self.capacity
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for x in old_storage:
            while x is not None:
                self.insert(x.key, x.value)
                x = x.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
