class HashTable:
    def __init__(self):
        self.size = 11
        self.capacity = self.size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def put(self, key, value):
        hash_value = self.hash_function(key, len(self.keys))

        if self.capacity < 1:
            self.keys += [None]
            self.values += [None]
            self.capacity += 1

        if self.keys[hash_value] is None:
            self.keys[hash_value] = key
            self.values[hash_value] = value
            self.capacity -= 1
        else:
            if self.keys[hash_value] == key:
                self.values[hash_value] = value
            else:
                rehashed = self.rehash(hash_value, len(self.keys))
                while self.keys[rehashed] is not None and self.keys[rehashed] != key:
                    rehashed = self.rehash(rehashed, len(self.keys))
                if self.keys[rehashed] is None:
                    self.keys[rehashed] = key
                    self.values[rehashed] = value
                    self.capacity -= 1
                else:
                    self.values[rehashed] = value

    def get(self, key):
        start_key = self.hash_function(key, len(self.keys))
        value = None
        found = False
        stop = False
        position = start_key
        while self.keys[position] is not None and not found and not stop:
            if self.keys[position] == key:
                value = self.values[key]
                found = True
            else:
                position = self.rehash(position, len(self.keys))
                if position == start_key:
                    stop = True
        return value

    def __delitem__(self, key):
        hash_value = self.hash_function(key, len(self.keys))

        if self.keys[hash_value] == key:
            self.keys[hash_value] = None
            self.values[hash_value] = None
        else:
            rehashed = self.hash_function(hash_value, len(self.keys))
            while self.keys[rehashed] != key:
                rehashed = self.hash_function(rehashed, len(self.keys))
            if self.keys[rehashed] == key:
                self.keys[rehashed] = None
                self.values[rehashed] = None

    def __contains__(self, key):
        return key in self.keys

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)
