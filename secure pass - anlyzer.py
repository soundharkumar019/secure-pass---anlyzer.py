def is_good_password(password):
    if len(password) < 8:
        return "Password too short. Must be at least 8 characters."

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*()":
            has_special = True

    if not has_upper:
        return "Password should have at least one uppercase letter."
    if not has_lower:
        return "Password should have at least one lowercase letter."
    if not has_digit:
        return "Password should have at least one number."
    if not has_special:
        return "Password should have at least one special character (!@#$%^&*())."

    return "Password is good!"

# Example usage
password = input("Enter your password: ")
result = is_good_password(password)
print(result)




#OUTPUT 
Enter your password: Pass123!
Password is good!

