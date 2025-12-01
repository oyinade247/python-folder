def larger_element(numbers):
    max = numbers[0]
    for index in range(0,len(numbers)):
        if numbers[index] > max:
            max = numbers[index]
    return max

numbers = [1,2,3,4,5,6]
print(larger_element(numbers))