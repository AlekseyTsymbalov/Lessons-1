# Задача "все ли равны?":
first = int(input("Введите первое целочисленное значение: "))
second = int(input("Введите второе целочисленное значение: "))
third = int(input("Введите третье целочисленное значение: "))

if first == second == third:
    print("3")
elif first == second or first == third:
    print("2")
elif second == first or second == third:
    print("2")
elif third == second or third== first:
    print("2")
else:
    print("0")