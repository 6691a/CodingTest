def solution(n):
    cache = []
    cache.insert(0, 1)
    cache.insert(1, 2)
    cache.insert(2, 3)

    if n < 4:
        return cache[n - 1]

    for i in range(3, n):
        cache.insert(i, (cache[i - 1] + cache[i - 2])% 1000000007)

    return cache[n - 1]

print(solution(9))
