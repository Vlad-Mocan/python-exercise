a = int(input("Enter a number: "))

if a > 0:
    print(f"{a} is a positive number.")
elif a < 0:
    print(f"{a} is a negative number.")
else:
    print(f"{a} is zero.")


if a % 2 == 0:
    print(f"{a} is an even number.")
else:
    print(f"{a} is an odd number.")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

letter = input("Enter a letter: ")

if letter in vowels:
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is a consonan.")

age = int(input("Enter your age: "))
if age < 18 or age > 65:
    print("You receive a discount!")
else:
    print("You don't receive a discount.")

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"Year {year} is a leap year!")
else:
    print(f"Year {year} is not a leap year.")
