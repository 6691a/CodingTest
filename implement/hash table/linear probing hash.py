class HashTable():
    def __init__(self, size: int):
        self.size = size
        self.hash_table = [[] for i in range(size)]

    
    def add(self, key, value):
        key = hash(key)
        hash_index = key % self.size

        if self.hash_table[hash_index]:
            for i in range(hash_index, len(self.hash_table)):
                
                if not self.hash_table[i]:
                    self.hash_table[i] = [key, value]
                    return
                elif self.hash_table[i][0] == key:
                    self.hash_table[i][1] = value
                    return
        else:
            self.hash_table[hash_index] = [key, value]

    def get(self, key):
        key = hash(key)
        hash_index = key % self.size
        if self.hash_table[hash_index] :
            for i in range(hash_index, len(self.hash_table)):
                if not self.hash_table[i]:
                    return None
                elif self.hash_table[i][0] == key:
                    return self.hash_table[i][1]

    def print(self):
        print(self.hash_table)

h = HashTable(5)
# print(hash("dk") % 5)
# print(hash("de") % 5)
h.add("dk", 100)
h.add("de", 1000)
h.add("dk", 200)




h.print()
