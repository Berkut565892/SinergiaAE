import collections

pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def get_suffix(age):
    if age % 10 == 1 and age != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age < 10 or age > 20):
        return "года"
    else:
        return "лет"

def pets_list():
    for pet_id, pet_info in pets.items():
        for pet_name, pet_data in pet_info.items():
            print(f"ID: {pet_id}")
            print(f"Имя питомца: {pet_name}")
            print(f"Вид питомца: {pet_data['Вид питомца']}")
            print(f"Возраст питомца: {pet_data['Возраст питомца']} {get_suffix(pet_data['Возраст питомца'])}")
            print(f"Имя владельца: {pet_data['Имя владельца']}")
            print("\n")

def create():
    last = collections.deque(pets, maxlen=1)[0]
    new_pet_name = input("Введите кличку питомца: ")
    new_pet_species = input("Введите вид питомца: ")
    new_pet_age = int(input("Введите возраст питомца: "))
    new_pet_owner = input("Введите имя владельца: ")
    pets[last + 1] = {new_pet_name: {"Вид питомца": new_pet_species, "Возраст питомца": new_pet_age, "Имя владельца": new_pet_owner}}

def update(ID):
    if get_pet(ID):
        pet_to_update = get_pet(ID)
        
        updated_pet_name = input("Введите новую кличку питомца: ")
        updated_pet_species = input("Введите новый вид питомца: ")
        updated_pet_age = int(input("Введите новый возраст питомца: "))
        updated_pet_owner = input("Введите новое имя владельца: ")

        pet_to_update[updated_pet_name] = {"Вид питомца": updated_pet_species, "Возраст питомца": updated_pet_age, "Имя владельца": updated_pet_owner}
        del pet_to_update[pet_to_update]

def delete(ID):
    if get_pet(ID):
        del pets[ID]

command = ""
while command != "stop":
    command = input("Введите команду (create, read, update, delete, list, stop): ")

    if command == "create":
        create()
    elif command == "read":
        pet_id = int(input("Введите ID питомца: "))
        pet = get_pet(pet_id)
        if pet:
            for pet_name, pet_info in pet.items():
                print(f"Это {pet_info['Вид питомца']} по кличке \"{pet_name}\". Возраст питомца: {pet_info['Возраст питомца']} {get_suffix(pet_info['Возраст питомца'])}. Имя владельца: {pet_info['Имя владельца']}")
    elif command == "update":
        pet_id = int(input("Введите ID питомца: "))
        update(pet_id)
    elif command == "delete":
        pet_id = int(input("Введите ID питомца: "))
        delete(pet_id)
    elif command == "list":
        pets_list()