team = ("Red Bull", "Mercedes", "Ferrari")
print(team[0])
print(team[2])
# team.add("McLaren") # 튜플은 값 추가 불가

(name, age, team) = ("Hamilton", 36, "Mercedes")
print(name, age, team)

F1 = {"Hamilton", "Verstappen", "Leclerc"}
F2 = set(["Leclerc", "Perez"])
# 교집합
print(F1 & F2) 
print(F1.intersection(F2)) 
# 합집합
print(F1 | F2) 
print(F1.union(F2)) 
# 차집합
print(F1 - F2) 
print(F1.difference(F2))

F1 = {"Hamilton", "Verstappen", "Leclerc"}
print(F1, type(F1))

F1 = list(F1)
print(F1, type(F1))

F1 = tuple(F1)
print(F1, type(F1))

F1 = set(F1)
print(F1, type(F1))