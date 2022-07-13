# 재귀함수는 스택의 형태로 관리됨

# 방식1
def factorial1(value: int) -> int:
    if value == 1:
        return 1
    
    return value * factorial1(value - 1)

# 방식2
def factorial2(value: int) -> int:
    if value == 1:
        return 1
    res = value * factorial2(value - 1)
    return res

print(factorial1(3))
print(factorial2(3))

def sum(data: list[int]) -> int:
    if len(data) == 1:
        return data[0]
    return data[0] + sum(data[1:])


print(sum([1, 2, 3, 4, 5]))

# 회문을 판단 할 수 있는 프로그램을 만드시오
def is_palindrome(string: str) -> bool:
    if len(string) <= 1:
        return True
    
    if string[0] == string[-1]:
        return is_palindrome(string[1 : -1])
    else:
        return False


print(is_palindrome("levvel"))

