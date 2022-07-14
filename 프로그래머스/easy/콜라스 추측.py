def func(num: int):
    ctn = 0
    def inner(value: int):
        nonlocal ctn
        if value == 1:
            return ctn
        if ctn > 500:
            return -1

        if value % 2 == 0:
            ctn += 1
            return inner(int(value / 2))
        else:
            ctn += 1
            return inner(3 * value + 1)
    return inner(num)

print(func(6))