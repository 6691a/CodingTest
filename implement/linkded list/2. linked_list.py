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
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self, value):
        self.head = Node(value)
        self.count = 1
    
    def add(self, value):
        node = self.head
        if not node:
            self.head = Node(value)
            self.count += 1

            return 

        while node.next:
            node = node.next
        node.next = Node(value)
        self.count += 1
    
    def delete(self, value):
        """
        1. head 노드를 삭제
        2. 중간 노드를 삭제
        3. 마지막 노드 삭제
        """
        if self.head.value == value:
            self.head = self.head.next
            self.count -= 1
            return 

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                self.count -= 1
                return  
            node = node.next


    def desc(self):
        node = self.head
        while node: 
            print(node.value)
            node = node.next
        
        if not self.head:
            print("노드가 존재하지 않습니다.")
        


l = LinkedList(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.delete(2)
l.delete(1)
l.delete(3)
l.delete(4)
l.delete(5)

l.desc()
l.add(6)
l.desc()
