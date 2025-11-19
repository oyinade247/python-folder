def get_length(list):
    count  = 0
    for number in list:
        if number == number:
            count += 1
    return count

number = [1,2,3,4,5]
print(get_length(number))