
def reverse_user_input(user_input):
    new_list = []
    # print(new_list)
    for _ in range(len(user_input)):
        remainder = int(user_input) % 10
        new_list.append(remainder)
        user_input = int(user_input) / 10
    return new_list

def sum_numbers(new_list):
    double  = double_second_digit(new_list)
    sum_double  = sum_second_digit(double)
    return sum_double

def double_second_digit(new_list):
    second_digit = []
    for digit in range(-2,len(new_list),2):
        remainder2 =  digit * 2
        if remainder2 > 9:
            remainder2 -= 9
        second_digit.append(remainder2)
    return second_digit


def sum_second_digit(second_digit):
    sum = 0
    for digit in range (len(second_digit)):
        sum += second_digit[digit]
    return sum

def add_odd_digit(new_list):
    odd_digit = []
    for digit in range(len(new_list),):
        pass






number = input("Enter your credit card number: ")
print(sum_numbers(number))