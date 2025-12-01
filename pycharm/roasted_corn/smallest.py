def smallest(numbers):
    smallest = numbers[0]
    for index in range(0,len(numbers)):
        if numbers[index] < smallest:
            smallest = numbers[index]
    return smallest

numbers = [1,2,3,4,5,6]
print(smallest(numbers))