
def buble_sort(data: list[int]):
    for i in range(len(data) - 1):
        is_sort = False
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                is_sort = True
        if not is_sort:
            break
    print(data)

data = [5,1,3,6,9,8]
buble_sort(data)