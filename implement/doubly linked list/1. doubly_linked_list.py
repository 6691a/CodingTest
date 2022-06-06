class Node():
    def __init__(self, data, forward=None, next=None):
        self.forward = forward
        self.next = next
        self.data = data
    

class DoubleLinkedList():
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.count = 1

    def all(self):
        node = self.head
        while node: 
            print(node.data)
            node = node.next
        if not self.head:
            print("노드가 존재하지 않습니다.")

    def all_tail(self):
        tail = self.tail

        if not self.tail:
            print("노드가 존재하지 않습니다.")

        while tail:
            print(tail.data)
            tail = tail.forward

    def append_head(self, data):
        if not self.head:
            self.head = Node(data, forward=self.head)
            self.tail = self.head
            self.count += 1
        
        head = self.head
        head.forward = Node(data, next=self.head)
        self.head = head.forward 
        self.count += 1

    def append_tail(self, data):
        if not self.head:
            self.head = Node(data, forward=self.head)
            self.tail = self.head
            self.count += 1
        
        node = self.tail
        node.next = Node(data, forward=node)
        self.tail = node.next
        self.count += 1
    
    def append_front(self, target: Node, data):
        front = target.forward

        new = Node(data, forward=target.forward, next=target)
        if target == self.head:
            self.head = new
        
        target.forward = new
        front.next = new

    def append_back(self, target: Node, data):
        back = target.next
        new = Node(data, forward=target, next=target.next)
        
        if target == self.tail:
            self.tail = new
        target.next = new
        back.forward = new


    def find_head(self, data) -> Node:
        head = self.head
        while head:
            if head.data == data:
                return head
            head = head.next
        
    def find_tail(self, data) -> Node:
        tail = self.tail
        while tail:
            # print(tail.data)

            if tail.data == data:
                return tail
            tail = tail.forward
   

a = DoubleLinkedList(0)
for i in range(1, 4):
    a.append_tail(i)
a.append_front(a.find_head(2), 1.5)
a.append_back(a.find_tail(1.5), 1.7)

a.all()
# a.all_tail()
