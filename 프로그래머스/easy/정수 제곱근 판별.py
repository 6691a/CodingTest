import math

def solution(n):
    # sqrt = math.sqrt(n)

    sqrt = n ** 0.5
    if sqrt % 1 == 0:
        return int((sqrt + 1) ** 2)
    
    return -1

solution(121)
solution(3)
