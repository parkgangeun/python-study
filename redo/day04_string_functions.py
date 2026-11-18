sentence = '피곤하다'
print(sentence)
sentence2 = "집 가고싶다"
print(sentence2)
sentence3 = """
피곤하고
집 가고싶다
"""
print(sentence3)

jumin = "090113-3456789"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리(뒤에서부터) : " + jumin[-7:])

Guabaa = "Pink guabba grape juice is good"
print(Guabaa.lower())
print(Guabaa.upper())
print(Guabaa[0].isupper()) 
print(len(Guabaa))
print(Guabaa.replace("good", "bad"))
index = Guabaa.index("u")
print(index)
index = Guabaa.index("u", index + 1)
print(index)
# print(Guabaa.index("Red"))
print(Guabaa.find("Red"))
print(Guabaa.count("u"))