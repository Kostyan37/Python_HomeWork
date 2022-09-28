# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


k = int(input("Insert k:   "))

fibList = [0] * (k * 2 + 1)
print(fibList)

fibList[k] = 0
fibList[k + 1] = 1

for i in range (k + 2, len(fibList)):
    fibList[i] = fibList[i - 2] + fibList[i - 1]

for i in range (k, -1, -1):
    fibList[i] = fibList[i + 2] - fibList[i + 1]

print(fibList)