# Day 2: 문자열 공부
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)
# 참 / 거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not (5>10))
# 애완동물을 소개해 주세요~
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3
print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))
# 퀴즈 1
station = "사당"
print(station + "행 열차가 들어오고 있니다")
#연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2
print(2**3) #2^3 = 8
print(5%3) # 나머지 구하기 2
print(5//3) # 몫 구하기 1
print( 10 > 3) # True
print( 4 >= 7) # False
print( 10 < 3) # False
print( 5 <= 5) # True
print( 3 == 3) # True
print( 4 == 2) # False
print( 3 + 4 == 7) # True
print( 1 != 3) # True
print(not(1 != 3)) # False
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True
print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True
print( 5 > 4 > 3) # True
print( 5 > 4 > 7) # False
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18
print(number)
number -= 2 #16
print(number)
number %= 5 # 1
print(number)
print(abs(-5)) # 5
print(pow(4, 2)) #4^2 = 4*4 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5
from math import *
print(floor(4.99)) # 내림. 4
print(ceil(3.14)) # 올림. 4
print(sqrt(16)) # 제곱근. 4
from random import *
# print(random()) # 0.0 ~ 1.0 미만으 임의의 값 생성
# print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10 + 1)) # 1 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10 + 1))
# print(int(random() * 10 + 1))
# print(int(random() * 10 + 1))
print(int(random() * 45 + 1)) # 1 ~ 45 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 28)) # 1 ~ 28 이하의 임의의 값 생성
# print("오프라인 스터디 모임 날짜는 매월" + str(randint(1, 28)) + "일로 선정되었습니다.")
# 퀴즈 2
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")
# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
 # 슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2 직전까지 (0, 1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일" + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지")
# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))
index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)
print(python.find("Java")) # 찾는 문자열이 없으면 -1 반환
# print(python.index("Java")) # 찾는 문자열이 없으면 오류 발생
print(python.count("n"))
print("a" + "b")
print("a", "b")
# 방법 1
# print("나는 %d살입니다." % 20) # 정수
# print("나는 %s을 좋아해요." % "파이썬") # 문자열
# print("Apple은 %c로 시작해요." % "A") # 문자
# %s
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))
# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color="빨간", age=20))
# 방법 4 (v3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#\n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
#\"\' : 문장 내에서 따옴표"
# 저는 "나도코딩"입니다."
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
# print("C:\\Users\\user\\Desktop\\PythonWorkspace")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")

# 퀴즈 3
# url = "http://naver.com"
url = "http://yotube.com"
my_str = url.replace("http://", "") # 규칙1
# print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙2
# my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1}입니다." .format(url, password)) 