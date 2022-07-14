# 정수 n이 홀수이면 3 * n + 1
# 짝수라면 n / 2
# n의 값이 1이 될때까지 반복하며 모든 값을 출력한다.

def func(num: int):
    print(num)
    if num <= 1:
        return num
    
    if num % 2 == 0:
        return func(int(num / 2))
    else:
        return func(3 * num + 1)

# func(3)

# 정수 n이 입력되면 n을 1, 2, 3 세 숫자를 갖고 나타낼 수 있는 경우의 수를 구하시오
# 정수 4의 1, 2, 3의 경우의 수
# 1 + 1 + 1 + 1
# 1 + 1 + 2
# 1 + 2 + 1
# 2 + 1 + 1
# 2 + 2
# 1 + 3
# 3 + 1


def func2(num: int) -> int:
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return func2(num -1) + func2(num -2) + func2(num -3)

print(func2(4))
print(func2(5))
