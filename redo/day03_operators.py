print(2**4)
print(100/5)
print(5//2) # 몫
print(5%2) # 나머지
print(5 < 7) # True
print(5 > 8) # False
print(8 <= 8) # True
print(3 == 3) # True
print(3 != 1) # True
print(not (3 != 1)) # False
print((3<0) and (3>2)) # False
print((3<5) & (3>1)) # True
print(not (3<5) & (3>1)) # False
print((3<5) or (3>4)) # True
print((3<5) | (3>4)) # True
print(not (3<5) | (3>4)) # False

print(3 * 2 + 3)
print((3 + 2) * 2) # 10
number = (3 + 2) * 2 # 10
print(number)
# number = number + 3
# print(number)
number += 3 # 13
print(number)
number *= 2 # 26
print(number)
number /= 2 # 13
print(number)
number %= 3 # 1
print(number)

print(abs(-2))
print(pow(5, 2)) # 제곱. 5^2
print(max(3, 14)) # 최대. 14
print(min(3, 14)) # 최소. 3
print(round(3.1)) # 반올림. 3
print(round(3.88)) # 4

from math import *
print(floor(3.88)) # 내림. 3
print(ceil(3.1)) # 올림. 4
print(sqrt(25)) # 제곱근. 5
print(sqrt(100)) # 10

from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 함수
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 함수
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 수 
print(int(random() * 10 + 1)) # 1 ~ 10 이하의 임의의 수
print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 수
print(randrange(1, 45)) # 1 ~ 45 미만의 임의의 수
# print(randrange(1, 45))
# print(randrange(1, 45))
# print(randrange(1, 45))
print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 수
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 수

# quiz
# 조건1: 랜덤으로 날짜를 뽑아야 함
# 조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외
# (출력문 예제) 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")