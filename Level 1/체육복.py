def solution(n, lost, reserve):
    

    ls = set(lost) - set(reserve)
    print(ls)
    re = set(reserve) - set(lost)
    print(re)
    for i in re:

        if i-1 in ls:
            ls.remove(i-1)
            
        elif i+1 in lost:
            ls.remove(i+1)
    
    return n - len(ls)


# solution(5,[2,4],[1,3,5])
# solution(5,[2,4],[3])
# solution(3,[3],[1])
