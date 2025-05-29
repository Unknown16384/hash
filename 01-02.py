class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    def hash_function(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return True
        return False

    def resize(self, size):
        old = self.table
        self.size = size
        self.table = [[] for _ in range(size)]
        for i in old:
            for pair in i:
                self.insert(*pair)

table = HashTable(5)
table.insert(1, 'a')
table.insert(2, 'b')
table.insert(3, 'c')
table.insert(4, 'd')
table.insert(5, 'e')
table.insert(6, 'f')
table.insert(7, 'g')
table.insert(8, 'h')
table.insert(9, 'i')
table.insert(0, 'j')
print(table.table)
table.resize(10)
print(table.table)