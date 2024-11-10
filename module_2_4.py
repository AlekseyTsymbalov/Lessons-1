import math
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for digits in numbers:
    is_prime = True

    if digits < 2:
        is_prime = False
        continue

    for  divider in range(2, int(math.sqrt(digits)) + 1):
        if digits % divider == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(digits)
    else:
        not_primes.append(digits)

print(f"Исходный код:\nnumbers = {numbers}")
print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")

# Пока, такие вот задачи даются кровью прям из глаз и ушей.
# Учёл ваше замечание касаемо названия переменных. Все в нижнем регистре.