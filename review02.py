import math

print(pow(2, 10)) # 제곱
print(7 % 3) # 나머지
print(7 // 3) # 몫

import random
print(random.randint(1, 45)) # 1 ~ 45 이하의 임의의 정수
print(int(random.random() * 10)) # 0 ~ 10 미만의 임의의 정수

python = "Python is Amazing"
index = python.index("n")
print(python.index("n", index + 1)) # 두 번째 n 찾기
print(len(python))

jumin = "030505-3123456"
print(jumin[:6]) # 030505
print(jumin[-7:]) # 3123456

print("이름: 강은\n\"파이썬\"은 '재밌어요'")