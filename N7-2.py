def rearrange_array(arr):
    n = len(arr)
    temp = arr[-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp
    return arr

# Пример использования метода:
N = int(input("Введите число N: "))
numbers = list(map(int, input("Введите N чисел через пробел: ").split()))

result = rearrange_array(numbers)
print(*result)