def multiply_third_position(numbers):
    multiply = 1
    for index in range(0,len(numbers)):
        if numbers[index] % 3 == 0:
            multiply *= numbers[index]
    return multiply

numbers = [1,2,3,4,5,6]
print(multiply_third_position(numbers))