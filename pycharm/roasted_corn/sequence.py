def sequence(numbers):
    new_list = []
    for number in range(1,(numbers + 1)):
        new_list.append(number)
    return new_list

num = 15
print(sequence(num))