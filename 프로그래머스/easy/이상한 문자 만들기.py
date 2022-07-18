def solution(s):
    s = s.split(" ")
    res = []

    for i in s:
        for j in range(len(i)):
            if j % 2 == 0:
                res.append(i[j].upper())
            else:
                res.append(i[j].lower())
        res.append(" ")
    res.pop()
    return "".join(res)



