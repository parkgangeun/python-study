major = ["통계학", "컴퓨터공학", "경제학"]
print(major)

subject = ["통계학개론", "환경과인간", "감정이해와철학적치유"]
print(subject)
print(subject.index("감정이해와철학적치유"))
subject.append("삶과죽음의철학")
print(subject)
subject.insert(2, "교양세미나와토론")
print(subject)
print(subject.pop())
print(subject)

subject.append("감정이해와철학적치유")
print(subject)
print(subject.count("감정이해와철학적치유"))

cabinet ={3: "통계학개론", 7: "환경과인간"}
print(cabinet[3])
print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))
# print(cabinet[5])

cabinet = {"A-3": "통계학개론", "B-7": "환경과인간"}
print(cabinet["A-3"])
print(cabinet["B-7"])

cabinet["C-20"] = "감정이해와철학적치유"
print(cabinet)

del cabinet["B-7"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
