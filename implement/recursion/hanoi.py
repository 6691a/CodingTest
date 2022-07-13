# 옮길 수 있는 공간(기둥)은 3개 이다.
# 크기가 다른 원반 n개를 시작 기둥에서 도착 기둥으로 모두 옮겨야 한다.
# 원반은 한 번에 한 개씩만 옮길 수 있다.
# 원반을 뽑을 땐 기둥의 맨 위의 원반을 뽑아야 한다. (중간에 있는 원반은 어떤 경우에도 뽑을 수 없다.)
# 원반을 쌓을 땐 기둥의 맨 위에 쌓아야 한다. (원반과 원반 사이에 끼워 넣을 수 없다.)
# 원반을 쌓을 땐 큰 원반 위에 작은 원반을 올려야 한다. (작은 원반 위에 큰 원반을 올릴 수 없다.)

def func (num: int, first: int, second: int, third: int) -> int:
    if num == 1:
        print(f"{first}에서 {third}로 이동")
        return 
    else:
        func(num - 1, first, third, second)
        print(f"{first}에서 {third}로 이동")
        func(num - 1, second, first, third)
        

func(2, "기둥1", "기둥2", "기둥3")
print(" ====== ")
func(3, "기둥1", "기둥2", "기둥3")
