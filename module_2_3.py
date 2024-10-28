my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0

while index < len(my_list):

    if my_list[index] < 0:
        break

    if my_list[index] == 0:
        index += 1
        continue

    print(my_list[index])

    index += 1

print("")
# А можно ещё так.

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0

while index < len(my_list):

    elem = my_list[index]
    index += 1

    if elem < 0:
        break

    if elem == 0:
        continue

    print(elem)