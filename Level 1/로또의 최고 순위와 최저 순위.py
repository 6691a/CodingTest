def solution(lottos, win_nums):
    cnt = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)
    return [7 - max(cnt + zero, 1) ,7 - max(cnt, 1)]


lottos1 = [44, 1, 0, 0, 31, 25]
lottos2 = [0, 0, 0, 0, 0, 0]
lottos3 = [44, 1, 0, 0, 31, 25]

win_nums1 = [31, 10, 45, 1, 6, 19]
win_nums2 = [38, 19, 20, 40, 15, 25]
win_nums3 = [20, 9, 3, 45, 4, 35]

solution(lottos2, win_nums1)

