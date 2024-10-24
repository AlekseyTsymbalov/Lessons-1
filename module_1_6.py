# Создаю свой словарь и вывожу в терминал.
print("\033[92m Работа со словарём\033[0m\n")
my_dict = {"Sasha" : 1987, "Ivan" : 1990, "Edik" : 1991, "Dasha" : 1999}
print(my_dict)
# Вывожу одно значение по существующему ключу
print(my_dict["Dasha"])
# Обращение к несуществующему ключу с выводом без ошибки
print(my_dict.get("Maksim"))
# А можно с обозначением, хотя и ненужно такое баловство.
print(my_dict.get("Maksim", "\033[91mТакого ключа нет: Maksim\033[0m"))
# Добавляю две произвольные пары в словарь
my_dict.update({"Angelina" : 1990, "Alina" : 1992})
hiding = my_dict.pop("Sasha")
print(f"Не существующее значение: {hiding}")
print(f"Изменённый список: {my_dict}\n")
print("************************************************************************************************\n")
# Работа с множествами.
print("\033[92m Работа с множествами \033[0m\n")
my_set = {1, 2, 3, 8.5, 1, 2, 3, "Pasha", "Sergey", "Pasha", "Sergey"}
print(set(my_set))
# Добавляем элементы
my_set.update((55, 77, 99))
# Удаляем элемент
my_set.discard(8.5)
print(f"Изменённое множество: {my_set}")