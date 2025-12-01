import random

word =  "AAA-###-@@"
for letter in word:
    splitted = word.split("-")
    new_letter = ""

    for char in splitted:
        combine = ""
        if char.isalpha():
            for i in range(0,3):
                character1 = chr(random.randint(65, 90))
                combine += character1
            new_letter += combine + "-"

        if not char.isalnum():
            combined = ""
            for j in range(0,3):
                character2 = (random.randint(1,10))
                combined += str(character2)
            new_letter += combined + "-"

        if char == "@@":
            combines = ""
            for r in range(0,3):
                character3 = chr(random.randint(97,105))
                combines += character3
            new_letter  += combines

print(new_letter)
