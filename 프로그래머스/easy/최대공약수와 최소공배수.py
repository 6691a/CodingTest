# https://codingpractices.tistory.com/34
def solution(n, m):
    res = []
    # 최대 공약수
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            res.append(i)
            break
    # 최소 공배수
    for i in range(max(n, m), n * m + 1):
        if i % n == 0 and i % m == 0:
            res.append(i)
            break
    print(res)
    return res

solution(3, 12)