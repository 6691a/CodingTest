
def solution(lottos, win_nums):
    ctn = 0
    for i in lottos:
        if i in win_nums:
            ctn += 1
    return [6 - max(lottos.count(0) + ctn, 1) + 1, 6 - max(ctn, 1) + 1]

    

# solution(
#     [44, 1, 0, 0, 31, 25],
#     [31, 10, 45, 1, 6, 19]
# )
# solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
solution([38, 19, 20, 40, 15, 25], [38, 19, 20, 40, 15, 25])
