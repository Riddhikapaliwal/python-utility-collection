class HashTable:

    def __init__(self):
        self.collection = {}

    def hash(self, string):
        hash_value = 0
        for char in string:
            hash_value += ord(char)
        return hash_value

    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value not in self.collection:
            self.collection[hash_value] = {key: value}
        else:
            self.collection[hash_value][key] = value

    def remove(self, key):
        h = self.hash(key)
        if h in self.collection and key in self.collection[h]:
            del self.collection[h][key]

    def lookup(self, key):
        h = self.hash(key)
        if h in self.collection:
            return self.collection[h][key]
        else:
            return None

