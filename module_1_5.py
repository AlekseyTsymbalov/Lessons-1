immutable_var = (333, 777, 999, True, "Коты", "Воин")
print(immutable_var)
# КЛЮЧЕВОЕ отличие от списка в ТОМ, что элементы внутри кортежа неизменяемые
# он САМ по себе является неизменяемой коллекцией. НО внтури может содержать
# изменяемые объекты ОСОБЕННОСТЬ неизменяемость, упорядоченность, разные элементы
# внутри кортежа могут храниться

mutable_list = [333, 777, 999, True, "Коты", "Воин"]
print(mutable_list)
mutable_list.append("Modified")
print(mutable_list)