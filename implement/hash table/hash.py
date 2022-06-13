
class HashTable():
    def __init__(self, size: int):
        self.size = size
        self.hash_table = [0 for i in range(size)]
    
    def add(self, key, value):
        hash_key =  hash(key) % self.size
        self.hash_table[hash_key] = value
    
    def get(self, key):
        hash_key =  hash(key) % self.size
        return self.hash_table[hash_key]

    def print(self):
        print(self.hash_table)

h = HashTable(5)
h.add('Nana', 100)
h.add('Mong', 500)

h.get("Nana")
