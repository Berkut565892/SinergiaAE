# Читаем входные данные
N = int(input())
numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)

# Переворачиваем массив
numbers.reverse()

# Выводим перевернутый массив
for number in numbers:
    print(number)