def solution(nums):
    answer = len(nums) // 2
    data = len(set(nums))

    if answer > data:
        return data
    return answer