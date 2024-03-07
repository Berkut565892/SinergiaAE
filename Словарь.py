# Создаем пустой словарь pets
pets = {}

# Запрашиваем у пользователя информацию о питомце
pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

# Добавляем информацию о питомце в словарь pets
pets[pet_name] = {
    "Вид питомца": pet_type,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

# Проверяем правильное склонение для возраста питомца
if pet_age % 10 == 1 and pet_age % 100 != 11:
    age_suffix = "год"
elif 2 <= pet_age % 10 <= 4 and (pet_age % 100 < 10 or pet_age % 100 >= 20):
    age_suffix = "года"
else:
    age_suffix = "лет"

# Выводим информацию о питомце
print(f"Имя питомца: {pet_name}")
print(f"Вид питомца: {pet_type}")
print(f"Возраст питомца: {pet_age} {age_suffix}")
print(f"Имя владельца: {owner_name}")

# Выводим итоговый словарь pets
print("Итоговый словарь pets:")
print(pets)