class HashTable:
    def __init__(self):
        self.size = 100
        self.bucket = [None for _ in range(self.size)]

    def get(self, key):
        hash_key = hash(key) % self.size
        return self.bucket[hash_key]

    def set(self, key, value):
        hash_key = hash(key) % self.size
        self.bucket[hash_key] = value


class HashTableWithOpenHashing:
    def __init__(self, size):
        self.size = size
        self.bucket = [[] for _ in range(self.size)]

    def key_hashing(self, key):
        return hash(key) % self.size

    def get(self, key):
        hash_key = self.key_hashing(key)
        for t in self.bucket[hash_key]:
            if t[0] == key:
                return t[1]
        return None

    def set(self, key, value):
        hash_key = self.key_hashing(key)
        for i in range(len(self.bucket[hash_key])):
            if self.bucket[hash_key][i][0] == key:
                self.bucket[hash_key][i][1] = value
                return
        self.bucket[hash_key].append([key, value])


class HashTableWithCloseHashing:
    def __init__(self, size):
        self.size = size
        self.hash_table = [-1 for _ in range(self.size * 2)]

    def key_hashing(self, key):
        return hash(key) % self.size

    def get(self, key):
        hash_key = self.key_hashing(key)
        for i in range(hash_key, len(self.hash_table)):
            if self.hash_table[i] == -1:
                continue
            if self.hash_table[i][0] == key:
                return self.hash_table[i][1]
        return None

    def set(self, key, value):
        hash_key = self.key_hashing(key)
        for i in range(hash_key, len(self.hash_table)):
            if self.hash_table[i] == -1:
                self.hash_table[hash_key] = [key, value]
                return
            elif self.hash_table[i][0] == key:
                self.hash_table[i][1] = value


if __name__ == '__main__':
    kv1 = 'John Smith', '521-4321'
    kv2 = 'Lisa Smith', '521-1234'
