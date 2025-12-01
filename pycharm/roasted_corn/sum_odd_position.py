def sum_odd_position(numbers):
    add = 0
    for number in range(0,len(numbers)):
        if numbers[number] % 2 != 0:
            add += number
    return add




number = [1,2,3,4,5]
print(sum_odd_position(number))