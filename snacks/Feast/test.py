import random

word =  "AAA-###-@@"
for letter in range(len(word)):
    new_list = ""
    new_letter = word.split("-")
    for character in new_letter:
        if character.isalpha():
            combine = ""
            for _ in range(0, 3):
                string_char = chr(random.randint(68, 70))
                combine += string_char
            new_list += combine + "-"
        if not character.isalnum():
            combine = ""
            for _ in range(0, 3):
                string_char = random.randint(1, 10)
                combine += str(string_char)
            new_list += combine + "-"

        if character == "@@":
            combine = ""
            for _ in range(0, 3):
                string_char = chr(random.randint(97, 105))
                combine += string_char
            new_list += combine


print(new_list)
