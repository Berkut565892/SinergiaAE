m = int(input())  # максимальная масса, которую может выдержать одна лодка
n = int(input())  # количество рыбаков
weights = [int(input()) for _ in range(n)]  # вес каждого рыбака

weights.sort()  # сортировка весов
min_boats = 0  # минимальное количество лодок

left = 0  # указатель на начало списка
right = n - 1  # указатель на конец списка

while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1
    right -= 1
    min_boats += 1

print (min_boats)