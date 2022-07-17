def solution(n):
    cache = [0] * 1_000_001
    cache[0] = 1
    cache[1] = 2
    cache[2] = 3
    cache[3] = 5

    if n < 5:
        return cache[n - 1]
    
    for i in range(4, n):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[i] % 15746





