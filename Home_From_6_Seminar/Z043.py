# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


my_list = [1, 2, 3, 5, 1, 5, 3, 10]


result_list = []
for i in my_list:
    if my_list.count(i) == 1:
        result_list.append(i)
print(result_list)