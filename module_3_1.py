# Глобальная переменная для подсчета вызовов функций
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return length, upper, lower

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    string_lower = string.lower()
    return any(string_lower == item.lower() for item in list_to_search)

# Примеры вызова функций
print(string_info('Capybara'))          # Вывод: (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))        # Вывод: (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Вывод: True
print(is_contains('cycle', ['recycling', 'cyclic']))    # Вывод: False

# Вывод количества вызовов функций
print(calls)  # Вывод: 4

# Изменить условие задачи и уже не решу её...