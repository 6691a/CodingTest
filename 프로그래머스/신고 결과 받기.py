

def solution(id_list: list, report: list, k: int):
    report = list(set(report))
    cnt = {i: [] for i in id_list}
    answer = {i: 0 for i in id_list}
    for i in report:
        s = i.split(" ")
        cnt[s[1]].append(s[0])

    for i in cnt:
        v = cnt[i]
        if k <= len(cnt[i]):
            for j in v:
                answer[j] += 1
    print(list(answer.values()))
    return list(answer.values())

solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
    2
)

solution(
    ["con", "ryan"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3
)