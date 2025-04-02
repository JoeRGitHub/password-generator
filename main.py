import random
import string
from os import system

letters = string.ascii_lowercase  # a-z
letters_upper = string.ascii_uppercase  # A=Z
digits = string.digits  # 0-9
punctuation = string.punctuation  # special characters
create_one_string = letters+digits+punctuation

print("Welcome to password generator 🔑")

while True:
    password_length_choice = input("Choose Password length: ")

    try:
        password_int = int(password_length_choice)
        if password_int <= 50 and password_int >= 8:
            break
        else:
            print("Oops! enter a number above 8 or below 50. Try again...")
    except ValueError:
        print("Oops!  That was no valid number. Try again...")


def password_lowercase():
    return string.ascii_lowercase


def password_uppercase():
    return string.ascii_uppercase


def password_digits():
    return string.digits


def password_punctuation():
    return string.punctuation


user_choice = {
    "lowercase": "yes",
    "uppercase": "yes",
    "numbers": "yes",
    "symbols": "yes"
}

option = {
    "lowercase": password_lowercase(),
    "uppercase": password_uppercase(),
    "numbers": password_digits(),
    "symbols": password_punctuation()
}
print("""How strong would you like your password to be?
      
Choose from the following options (Yes\Enter or No):>
      """)

while True:
    password_customize_lowercase = input("Lowercase? \n").lower()
    password_customize_uppercase = input("Uppercase? \n").lower()
    password_customize_numbers = input("Numbers? \n").lower()
    password_customize_symbols = input("Symbols? \n\n").lower()

    if password_customize_lowercase != "no":
        print("Lowercase: Yes")
    else:
        user_choice['lowercase'] = "no"
        print(f"Lowercase: {password_customize_lowercase}")

    if password_customize_uppercase != "no":
        print(f"Uppercase: Yes")
    else:
        user_choice['uppercase'] = "no"
        print(f"Uppercase: {password_customize_uppercase}")

    if password_customize_numbers != "no":
        print("Numbers: Yes")
    else:
        user_choice['numbers'] = "no"
        print(f"Numbers: {password_customize_numbers}")

    if password_customize_symbols != "no":
        print("Symbols: Yes\n")
    else:
        user_choice['symbols'] = "no"
        print(f"Symbols: {password_customize_symbols}\n")

    check_user_choice = input(
        "Continue or Reselect (Yes\Enter or Reselect):> \n").lower()
    if check_user_choice != "reselect":
        break
    else:
        system("clear||cls")

result_str = ""
for type, answer in user_choice.items():
    if answer == "yes":
        result_str += option[type]


s_shuffled = ''.join(random.sample(result_str, len(result_str)))

print(
    f"Copy your password to a safe place: \n{s_shuffled[0:password_int]}")
