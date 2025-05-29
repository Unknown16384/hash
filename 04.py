class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    def string_hash(self, string):
        return sum([ord(a) for a in str(string)])
    def insert(self, string):
        index = self.string_hash(string) % self.size
        for pair in self.table[index]:
            if pair[0] == string: return
        self.table[index].append([string, self.string_hash(string)])
    def search(self, string):
        index = self.string_hash(string) % self.size
        for pair in self.table[index]:
            if pair[0] == string: return pair[1]
        return None

table = HashTable(10)
table.insert('word')
table.insert('string')
print(table.search('word'))
print(table.search('string'))