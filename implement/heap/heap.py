# 힙 구현 시 배열 구조를 활용 함 (시작 인덱스를 1로 가정)
# 부모 노드의 인덱스 번호 : 자식 노드의 인덱스 // 2
# 왼쪽 자식 노드 인덱스 번호 : 부모노드 인덱스 * 2
# 오른쪽 자식 노드 인덱스 번호 : 부모노드 인덱스 * 2 + 1
# Max Heap으로 구현

from calendar import c


class Heap():
    def __init__(self, value: int):
        self.array = [None]
        self.array.append(value)

    def __is_move(self, current_index: int, parent_index: int) -> bool:
        if current_index <= 1:
            return False
        if self.array[current_index] > self.array[parent_index]:
            return True
        return False
        
    def insert(self, value: int):
        self.array.append(value)
        # 상위 노드와 비교 후 크다면 이동
        current_index = len(self.array) -1
        parent_index = current_index // 2
        
        while self.__is_move(current_index, parent_index):
            # 상위 노드와 현제 노드의 위치 변경
            self.array[parent_index], self.array[current_index] = self.array[current_index], self.array[parent_index]
            # 변경 후 현제 노드의 인덱스 값도 변경
            current_index = parent_index
            parent_index = current_index // 2

    def __is_down(self, current_index: int, left_child_index: int, right_child_index: int) -> bool:
        # 자식 노드가 없을 경우
        if len(self.array) <= left_child_index:
            return False
        # 왼쪽 자식 노드가 있을 경우
        elif len(self.array) <= right_child_index:
            # 현제 노드와 왼쪽 자식 노드의 값 비교
            if self.array[current_index] < self.array[left_child_index]:
                return True
            return False
        # 자식 노드가 모두 있다면
        else:
            if self.array[left_child_index] > self.array[right_child_index]:
                if self.array[current_index] < self.array[left_child_index]:
                    return True
                return False
            else:
                if self.array[current_index] < self.array[right_child_index]:
                    return True
                return False

        return False
    def pop(self) -> int:
        res = self.array[1]
        # 마지막에 추가된 값을 root로 변경
        self.array[1] = self.array[-1]
        del self.array[-1]

        current_index = 1
        left_child_index = current_index * 2
        right_child_index = current_index * 2 + 1
        while self.__is_down(current_index, left_child_index, right_child_index):
            if len(self.array) <= right_child_index:
                if self.array[current_index] < self.array[left_child_index]:
                    self.array[current_index], self.array[left_child_index] =  self.array[left_child_index], self.array[current_index]
                    current_index = left_child_index
            else:
                if self.array[left_child_index] > self.array[right_child_index]:
                    if self.array[current_index] < self.array[left_child_index]:
                        self.array[current_index], self.array[left_child_index] = self.array[left_child_index], self.array[current_index]
                        current_index = left_child_index

                else:
                    if self.array[current_index] < self.array[right_child_index]:
                        self.array[current_index], self.array[right_child_index] = self.array[right_child_index], self.array[current_index]
                        current_index = right_child_index

            left_child_index = current_index * 2
            right_child_index = current_index * 2 + 1
        return res

    
    def print(self):
        print(self.array)
        return self.array

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)

assert [None, 20, 10, 15, 5, 4, 8] == heap.print()

heap.pop()

assert [None, 15, 10, 8, 5, 4] == heap.print()
