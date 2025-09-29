num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

if num1 > num2:
    first_largest = num1
    second_largest = num2
else:
    first_largest = num2
    second_largest = num1

count = 3

while count <= 10:
    number = int(input(f"Enter number : "))

    if number > first_largest:
        second_largest = first_largest
        first_largest = number
    elif number > second_largest:
        second_largest = number

    count += 1

print(first_largest)
print(second_largest)