# 배열의 데이터 중 가장 작은 값을 찾는다
# 해당 최소값을 데이터 맨 앞의 값과 교체
# 변경한 데이터를 뺀 나머지 값을 위 내용을 반복한다


from xml.dom import minicompat


def sort(data: list[int]):
    for i in range(len(data) -1):
        min = i
        for j in range(i + 1, len(data)):
            if data[min] > data[j]:
                min = j
        data[min], data[i] = data[i], data[min]
    
    print(data)
    
sort([10, 2, 11, 25, 1, 3, 20, 5, 4])