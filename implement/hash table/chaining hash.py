class HashTable():
    def __init__(self, size: int):
        self.size = size
        self.hash_table = [[] for i in range(size)]
    
    def add(self, key, value):
        # hash_key =  hash(key)
        hash_key =  key
        target = self.hash_table[hash_key % self.size]
        if target:
            for i in range(len(target)):
                if target[i][0] == hash_key:
                    target[i][1] = value
                    return
                
        target.append([hash_key, value])

    
    def get(self, key):
        hash_key =  key
        target = self.hash_table[hash_key % self.size]
        if target:
            for i in range(len(target)):
                if target[i][0] == hash_key:
                    print(target[i][1])
                    return target[i][1]

    def print(self):
        print(self.hash_table)

h = HashTable(5)
h.add(1, 100)
h.add(11, 200)
h.add(111, 300)
h.add(1111, 400)
h.add(1, 10)

# h.print()
