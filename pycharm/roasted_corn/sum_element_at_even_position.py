def sum_even_element_position(numbers):
    add = 0
    for index in range(0,len(numbers)):
        if numbers[index] % 2 == 0:
            add += numbers[index]
    return add

numbers = [1,2,3,4,5]
print(sum_even_element_position(numbers))
