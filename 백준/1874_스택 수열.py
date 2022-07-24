def solution(data: list[int]):
    stack = []
    current = 1
    res = []
    for i in data:
        while i >= current:
            stack.append(current)
            res.append("push")
            current += 1
        if i == stack[-1]:
            stack.pop()
            res.append("pop")
        else:
            return "NO"

    print(res)
    return res

solution([4, 3, 6, 8, 7, 5, 2, 1]) == ["push", "push", "push", "push", "pop", "pop", "push", "push", "pop", "push", "push", "pop", "pop", "pop", "pop", "pop"]