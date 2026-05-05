# [ 파이썬 기초 함수 ]

# 1. 숫자 관련 함수 (math 모듈 필요)
import math # 수학 함수용

print(abs(-5))      # 절댓값 5
print(pow(4, 2))    # 제곱 4^2 = 4*4 = 16
print(max(5, 12))   # 최댓값 12
print(min(5, 12))   # 최솟값 5
print(round(3.14))  # 반올림 3

# ★ 주의: 바닥(floor)과 천장(ceil)
print(math.floor(4.99)) # 내림: 바닥으로 감 4
print(math.ceil(3.14))  # 올림: 천장으로 감 4
print(math.sqrt(16))    # 제곱근 4.0

# 2. 랜덤 함수 (random 모듈 필요)
import random

print(random.random())         # 0.0 ~ 1.0 미만 실수
print(random.randrange(1, 46)) # 1 ~ 45 중 정수 (46 포함 X)
print(random.randint(1, 45))   # 1 ~ 45 중 정수 (45 포함 O)

# 3. 문자열 기본 함수
s = "Python is Amazing"

print(s.lower())        # 전체 소문자로
print(s.upper())        # 전체 대문자로
print(s.isupper())      # 대문자인지 확인 (True/False)
print(len(s))           # 문자열 길이 (글자 수)
print(s.replace("Python", "Java")) # 단어 교체

# 4. 문자열 찾기 (Index vs Find)
# index는 없으면 에러나서 프로그램 멈춤 / find는 없으면 -1 출력
print(s.find("n"))      # 처음 나오는 n의 위치
print(s.index("n"))     # 처음 나오는 n의 위치
print(s.count("n"))     # n이 몇 번 나오는지 세기

# 5. 문자열 슬라이싱 (중요!)
# [시작 : 끝 : 증감] -> '끝' 번호 직전까지 자름
jumin = "990120-1234567"
print(jumin[0:2])    # 0부터 2 직전까지 (99)
print(jumin[:6])     # 처음부터 6 직전까지 (990120)
print(jumin[7:])     # 7부터 끝까지 (1234567)
print(jumin[-7:])    # 뒤에서 7번째부터 끝까지

# 6. 문자열 포맷팅 (f-string 추천)
age = 20
color = "빨간"
# 방법 1: format 함수 사용 (인덱스 활용)
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # 순서 바꾸기 가능
# 방법 2: f-string (가장 편리함, v3.6 이상)
print(f"나는 {age}살이며, {color}색을 좋아해요.") # 변수 이름을 직접 넣음

# 탈출 문자 (특수 기능을 하는 문자들)
print("백문이 불여일견\n백견이 불여일타") # \n : 줄바꿈
print('저는 "나도코딩"입니다.') # 문장 내 따옴표 포함법
print("C:\\Users\\Desktop") # \\ : 문장 내에서 역슬래시(\) 자체를 표시

# 문자열 퀴즈 핵심 로직 
# 예: http://naver.com 에서 비밀번호 생성하기
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1: http:// 제거
my_str = my_str[:my_str.index(".")] # 규칙 2: 처음 만나는 점(.) 전까지만 자르기

# 규칙 3: 남은 글자 중 처음 3자리 + 총 글자 수 + 'e' 개수 + "!"
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(f"{url}의 비밀번호는 {password}입니다.")