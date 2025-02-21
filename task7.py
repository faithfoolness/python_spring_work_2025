#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

print("AC = ", abs(A - B))
print("BC = ", abs(B - C))
print("AB + BC = ", abs(A - B) + abs(B - C))
