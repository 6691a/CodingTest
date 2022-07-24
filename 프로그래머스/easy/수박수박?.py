def solution(n):
    str = ""
    for i in range(n):
        if i % 2 == 0:
            str += "수"
        else:
            str += "박"
    return str
solution(2)


