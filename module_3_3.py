def print_params(a=1, b="строка", c=True):
    print(a, b, c)

print_params() # Вызов без аргументов и она же вызов чисто этой самой функции
print_params(3, "Сила", False) # Переназначил для проверки
print_params(b=25) # Проверил и так IDE  пишет что ожидаемый тип один, а вместо него пришёл другой
print_params(c=[1, 2, 3])

print()

values_list = [7, "Утро", True]
values_dict = {"a": 42, "b": "Мир", "c": 16.78}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, "Строка"]
print_params(*values_list_2, 42)