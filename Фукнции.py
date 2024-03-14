def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorials_list(n):
    current_factorial = factorial(n)
    factorials = [current_factorial]
    for num in range(n-1, 0, -1):
        current_factorial *= num
        factorials.append(current_factorial)
    return factorials

number = 3 #Здесь указываем нужное нам число.
print("Исходное число:", number)

fact_number = factorial(number)
print("Факториал числа", number, "равен:", fact_number)

factorials_result = factorials_list(fact_number)
print("Список факториалов от", fact_number, "до 1:", factorials_result)