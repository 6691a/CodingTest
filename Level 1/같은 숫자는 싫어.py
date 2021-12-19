def solution(arr):
    answer = []

    answer.append(arr.pop(0))


    for i in arr:
       if answer[-1] == i:
           continue
       answer.append(i)

    return answer

solution([1,1,2,3,4])