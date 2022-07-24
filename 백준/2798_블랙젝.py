from itertools import combinations

def solution(nums: list[int], limit: int):
    res = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                val = nums[i] + nums[j] + nums[k]
                if val <= limit:
                    res = max(res, val)
    return res


def solution2(nums: list[int], limit: int):
    res = 0
    for i in combinations(nums, 3):
        if (val := sum(i)) <= limit:
            res = max(res, val)
    return res

assert solution([5, 6, 7, 8, 9], 21) == 21
assert solution2([5, 6, 7, 8, 9], 21) == 21

assert solution([93, 181, 245, 214, 315, 36, 185, 138, 216, 295], 500) == 497
assert solution2([93, 181, 245, 214, 315, 36, 185, 138, 216, 295], 500) == 497



