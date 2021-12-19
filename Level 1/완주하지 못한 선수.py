import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    print(list(answer)[0])
    return list(answer)[0]

solution(["leo", "kiki", "eden"],["eden", "kiki"])
