def solution(n):
    cache = [0] * 101
    cache[0] = 1
    cache[1] = 1
    cache[2] = 1
    cache[3] = 2 # cache[0] + cache[1]
    cache[4] = 2 # cache[1] + cache[2]
    cache[5] = 3 # cache[2] + cache[3]
    cache[6] = 4 # cache[3] + cache[4]
    cache[7] = 5 # cache[4] + cache[5]
    cache[8] = 7 # cache[5] + cache[6]
    cache[9] = 9 # cache[6] + cache[7]

    if n < 11:
        return cache[n - 1]

    for i in range(10, n):
        cache[i] = cache[i - 3] + cache[i - 2]

    return cache[n - 1]


assert solution(2) == 1
assert solution(6) == 3
assert solution(12) == 16




