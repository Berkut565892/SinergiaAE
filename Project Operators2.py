word = input("Введите слово из латинских букв: ")

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
consonants = 0

for letter in word:
    if letter in vowels:
        vowels[letter] += 1
    else:
        if letter.isalpha():
            consonants += 1
        else:
            print(False)

if not False:
    print("Гласных букв:", sum(vowels.values()))
    print("Согласных букв:", consonants)
    print("Количество каждой из гласных букв:")
    for vowel, count in vowels.items():
        print(f"{vowel}: {count}")
