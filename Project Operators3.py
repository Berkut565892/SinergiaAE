X = int(input("Введите минимальную сумму инвестиций X: "))
A = int(input("Введите сумму денег у Майкла A: "))
B = int(input("Введите сумму денег у Ивана B: "))

if A >= X and B >= X:
    print("2")
elif A >= X or B >= X:
    print("1")
else:
    print("0")