def get_average(numbers):
    add = 0
    average = 0
    for index in range(0,len(numbers)):
        add += numbers[index]
    average = add / len(numbers)
    return average

numbers = [1,2,3,4,5,6]
print(get_average(numbers))