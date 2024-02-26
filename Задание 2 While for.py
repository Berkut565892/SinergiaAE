import math

X = int(input("Введите число: "))
count = 0

for i in range(1, int(math.sqrt(X)) + 1):
    if X % i == 0:
        count += 1
        if X // i != i: # Проверяем, чтобы не учитывать дважды квадратный корень
            count += 1

print("Количество натуральных делителей:", count)