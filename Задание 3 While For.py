A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

for num in range(A, B+1):
    if num % 2 == 0:
        print(num, end=" ")