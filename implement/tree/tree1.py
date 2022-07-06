from calendar import c
from os import curdir
from re import L


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
            if current.value == value:
                return
            elif current.value > value:
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

    def delete(self, value):
        # 삭제 노드
        current = self.root
        # 삭제 노드의 부모 노드
        parent = self.root
        is_deleted = False
        while current:
            if current.value == value:
                is_deleted = True
                break
            elif current.value > value:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        
        if not is_deleted:
            return False
        
        # 1: node가 leaf인 경우
        if not current.left and not current.right:
            if parent.value > value:
                parent.left = None
            else:
                parent.right = None
            del current
        # 2: node가 child node를 1개 갖는 경우
        if current.left and not current.right:
            if parent.value > value:
                parent.left = current.left
            else: 
                parent.right = current.left
        elif not current.left and current.right:
            if parent.value > value:
                parent.left = current.right
            else: 
                parent.right = current.right
        # 3-1: node가 child를 2개 갖고 있는 경우
        if current.left and current.right:
            # 삭제 할 노드가 부모노드의 왼쪽에 존재
            if parent.value > value:
                target = current.right
                target_parent = current.right
                while target.left:
                    target_parent = target
                    target = target.left
                # 가장 작은 값의 노드에 오른쪽에 값이 있을 경우
                if target.right:
                    target_parent.left = target.right
                else:
                    target_parent.left = None
                # target을 삭제할 노드를 대신함
                parent.left = target
                target.left = current.left
                target.right = current.right
            # 삭제 할 노드가 부모노드의 오른쪽에 존재
            else:
                target = current.right
                target_parent = current.right
                while target.left:
                    target_parent = target
                    target = target.left
                if target.right:
                    target_parent.left = target.right
                else:
                    target_parent.left = None
                parent.right = target
                target.left = current.left
                target.right = current.right

from random import randint

# 테스트


data = [
    1, 514, 519, 16, 17, 539, 541, 44, 46, 559, 561,
    567, 68, 83, 596, 87, 600, 603, 95, 108, 621, 620,
    120, 124, 129, 643, 647, 138, 142, 656, 146, 670,
    675, 683, 684, 181, 185, 191, 708, 711, 734, 226,
    230, 745, 747, 237, 753, 248, 250, 764, 774, 272, 
    278, 792, 281, 283, 796, 289, 298, 314, 318, 832,
]

tree = Tree(500)

for i in data:
    tree.add(i)

for i in data:
    assert True == tree.get(i)


# [561, 567, 68, 83, 596, 87, 600, 603, 95, 108]
for i in data[10: 20]:
    tree.delete(i)

for i in data[10: 20]:
    assert False == tree.get(i)

