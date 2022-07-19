def solution(data: list[int]):
    if len(data) <= 1: 
        return data

    pivot = data[0]
    left = []
    right = []
    for i in data[1:]:
        if pivot > i:
            left.append(i)
        else:
            right.append(i)
    
    return solution(left) + [pivot] + solution(right)
    

print(solution([10, 1, 2, 7, 4, 20, 15, 14, 18])) 