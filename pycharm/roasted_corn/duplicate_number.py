def duplicate_num(numbers):
    new_list = numbers.copy()
    for item in new_list:
        numbers.append(item)

    return numbers



def remove_duplicate_num(numbers):
    new_list = []
    for item in numbers:
        if item not in new_list:
            new_list.append(item)
    return new_list

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
duplicate = duplicate_num(numbers)

print(remove_duplicate_num(duplicate))


def sum_third_element(numbers):
    add = 0
    for item in range(0,len(numbers)):
        if item % 3 == 0:
            add += numbers[item]
    return add

num =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,20]
duplicate_number = duplicate_num(num)
remove_duplicate_num = remove_duplicate_num(duplicate_number)
print(sum_third_element(remove_duplicate_num))
