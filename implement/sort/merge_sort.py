# 1. 리스트를 절반으로 나눈다.
# 2. 각 리스트를 재귀적으로 정렬한다.
# 3. 정렬된 리스트를 다시 하나의 리스트로 병합한다.
def split(data: list[int]) -> list[int]:
    if len(data) <= 1:
        return data
    half = int(len(data) / 2)
    left = data[:half]
    right = data[half:]

    print(left)
    print(right)
    
def merge(data1: list[int], data2: list[int]):
    ...
# def solution(data: list[int]):
#     ...

split([5, 21, 20, 1, 3, 6, 4, 7, 16, 12])