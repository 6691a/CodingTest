def solution(data: list[int]):
    if data[0] < data[1]:
        for i in range(2, len(data)):
            if data[i] < data[i - 1]:
                return "mixed"
        
        return "ascending"
    else:
        for i in range(2, len(data)):
            if data[i] > data[i - 1]:
                return "mixed"
        return "descending" 

assert "ascending" == solution([1, 2, 3, 4, 5, 6, 7, 8])
assert "descending" == solution([8, 7, 6, 5, 4, 3, 2, 1])
assert "mixed" == solution([8, 1, 7, 2, 6, 3, 5, 4])


# data = list(map(int, input().split(" ")))