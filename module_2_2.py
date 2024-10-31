# Задача "все ли равны?":
# first = int(input("Введите первое целочисленное значение: "))
# second = int(input("Введите второе целочисленное значение: "))
# third = int(input("Введите третье целочисленное значение: "))
#
# if first == second == third:
#     print("3")
# elif first == second or first == third:
#     print("2")
# elif second == first or second == third:
#     print("2")
# elif third == second or third== first:
#     print("2")
# else:
#     print("0")

# А можно проще получается вот так.
first = int(input("Введите первое целочисленное значение: "))
second = int(input("Введите второе целочисленное значение: "))
third = int(input("Введите третье целочисленное значение: "))

# Собираем значения в список и используем set для нахождения уникальных значений
unique_values = len(set([first, second, third]))

if unique_values == 1:
    print("3")
elif unique_values == 2:
    print("2")
else:
    print("0")