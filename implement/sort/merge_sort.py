# 1. 리스트를 절반으로 나눈다.
# 2. 각 리스트를 재귀적으로 정렬한다.
# 3. 정렬된 리스트를 다시 하나의 리스트로 병합한다.
from re import L


def split(data: list[int]) -> list[int]:
    if len(data) <= 1:
        return data

    half = int(len(data) / 2)
    left = split(data[:half])
    right = split(data[half:])

    return merge(left, right)
    
def merge(left: list[int], right: list[int]):
    res = []
    left_index, right_index = 0, 0
    while len(left) > left_index and len(right) > right_index:
        if left[left_index] > right[right_index]:
            res.append(right[right_index])
            right_index += 1
        else:
            res.append(left[left_index])
            left_index += 1
            

    if len(left) > left_index:
        res = res + left[left_index: ]
    else:
        res = res + right[right_index: ]

    # while len(left) > left_index:
    #     res.append(left[left_index])
    #     left_index += 1
    # while len(right) > right_index:
    #     res.append(right[right_index])
    #     right_index += 1
    return res


assert split([5, 21, 20, 1, 3, 6, 4, 7, 16, 12]) == [1, 3, 4, 5, 6, 7, 12, 16, 20, 21]
assert split([5, 21, 20, 1, 3, 6, 4, 7, 12]) == [1, 3, 4, 5, 6, 7, 12, 20, 21]
