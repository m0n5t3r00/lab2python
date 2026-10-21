#3
print("Hello, World!")

#4
name = "Анна"
age = 21
height = 1.68
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

name = "Анна"
age = 22
height = 1.69
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#5
first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")

raw_age = input("Введите возраст: ")
print("Тип возраста до преобразования:", type(raw_age))

age = int(raw_age)
height = float(input("Введите рост (например, 1.75): "))

print(f"Пользователь: {first_name} {last_name}, Возраст: {age} ({type(age)}), Рост: {height} ({type(height)})")

#6
a = 15
b = 4

print("Сложение:", a + b)
print("Вычитание:", a - b)
print("Умножение:", a * b)
print("Обычное деление (/):", a / b)
print("Целочисленное деление (//):", a // b)
print("Остаток от деления (%):", a % b)
print("Возведение в степень (**):", a ** b)

print(2 + (3 * 4))
print((2 + 3) * 4)

#7
x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))

print("Сумма:", x + y)
print("Разность:", x - y)
print("Произведение:", x * y)
if y != 0:
    print("Деление:", x / y)
else:
    print("Деление на ноль")

#8
for i in range(1, 11):
    print(i, end=" ")
print()

for i in range(10, 0, -1):
    print(i, end=" ")
print()

for i in range(0, 21, 2):
    print(i, end=" ")
print()

#9
n = int(input("Введите целое положительное число n: "))
x = 0

for i in range(1, n + 1):
    x += i

print(f"Сумма чисел от 1 до {n} равна: {x}")

#10
x = 10
while x >= 1:
    print(x)
    x -= 1
print("кц")

#11
import math

radius = float(input("Введите радиус круга: "))
circle = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print("Длина окружности:", round(circle, 2))
print("Площадь круга:", round(area, 2))
print("Квадратный корень из 12:", math.sqrt(12))

#12
number = int(input("число"))

if number > 0:
    print("положительное")
elif number < 0:
    print("отрицательное")
else:
    print("равно нулю")
if number % 2 == 0:
    print("чётное")
else:
    print("нечётное")

#13
age = int(input("Введите возраст: "))
has_access = input("Имеется ли допуск (да/нет): ").strip().lower() == "да"

if age >= 18 and has_access:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")

#14
n = int(input("Введите количество измерений: "))

if n > 0:
    total_sum = 0.0

    for i in range(1, n + 1):
        value = float(input(f"Введите измерение #{i}: "))
        total_sum += value

    average = total_sum / n

    print("\n--- Результаты анализа ---")
    print(f"Сумма всех измерений: {total_sum}")
    print(f"Среднее арифметическое: {average}")
else:
    print("Количество измерений должно быть больше 0.")