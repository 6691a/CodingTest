class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree():
    def __init__(self, value):
        self.root = Node(value)


    def add(self, value):
        current = self.root
        while True:
            if current.value > value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    break

    def get(self, value):
        current = self.root
        while current:
            if current.value == value:
                return True
            elif current.value > value:
                current = current.left
            else:
                current = current.right
        
        return False
    def all():
        ...

tree = Tree(10)

tree.add(5)
tree.add(11) 
tree.add(4)

print(tree.get(4))
print(tree.get(5))
print(tree.get(16))


# print(tree.root.__dict__)
# print(tree.root.left.__dict__)
# print(tree.root.left.left.__dict__)

# print(tree.root.right.__dict__)

