password = input("Enter your password: ")

contains_uppercase = False
contains_number = False

for letter in password:
    if letter.isupper():
        contains_uppercase = True
    if letter.isdigit():
        contains_number = True

if len(password) < 8:
    print("Weak Password! Password must have at least 8 characters.")
elif not contains_uppercase:
    print("Weak Password! Password must contain at least one uppercase letter.")
elif not contains_number:
    print("Weak Password! Password must contain at least one number.")
else:
    print("Strong password!")
