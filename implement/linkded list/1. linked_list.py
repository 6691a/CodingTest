"""
1.노드
    - 다음 노드를 가르킬 변수 필요
    - 값을 저장할 변수 필요

2. 링크드 리스트
    - 시작 노드를 갖고 있을 변수
    - 노드에 값을 추가 할 함수
    - 노드에 값을 삭제 할 함수

"""
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        self.head = Node(value)
        self.count = 0
    
    def append(self, value):
        node = self.head
        
        while node.next:
            node = node.next
        
        node.next = Node(value)
        self.count += 1
    
    def pop(self):
        node = self.head
        before = None
        for i in range(0, self.count):
            if i == self.count -1:
                before = node
            if node.next:
                node = node.next
        before.next = None
        return node.value
        
    def print_all(self):
        node = self.head

        while node:
            print(node.value)
            node = node.next

l = LinkedList(1)
l.append(2)
l.append(3)
l.append(4)

l.pop()

l.print_all()

l.append(5)

l.print_all()
