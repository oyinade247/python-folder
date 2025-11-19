def password_validator(password):
    upper = False
    lower = False
    digit = False

    if len(password) < 10:
        return "weak"
    else:
        upper = False
        lower = False
        digit = False
        symbol = False

    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True
        else:
            symbol = True

    if upper and lower and digit and symbol:
        return "strong"
    elif upper and lower and symbol and not digit:
        return "medium"

    return None


password = input("Enter password: ")
print(password_validator(password))
