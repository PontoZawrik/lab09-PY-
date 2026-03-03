from module import suml, prodl
from square import *

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones), end="\n\n")


print("1) Прямоугольник\n2) Треугольник\n3) Круг")
p = int(input("Площадь какой фигуры вы хотите вычислить: "))

if p == 1:
    a, b = map(int, input("Введите длину и ширину прямоугольника: ").split())
    print(f"Площадь прямоугольника: {rectangle_area(a, b)}")
elif p == 2:
    a, h = map(int, input("Введите основание и высоту треугольника: ").split())
    print(f"Площадь тремоугольника: {triangle_area(a, h)}")
elif p == 3:
    radius = int(input("Введите радиус круга: "))
    print(f"Площадь круга: {circle_area(radius)}")

