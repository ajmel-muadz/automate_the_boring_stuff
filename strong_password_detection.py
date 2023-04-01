# strong_password_detection.py - A program using regular expressions to
# detect if a password entered matches arbitrary constraints.

import re


def password_strength(password):
    # Defining regular expressions for lower/upper case and digits.
    lower_case_regex = re.compile(r"[a-z]+")
    upper_case_regex = re.compile(r"[A-Z]+")
    digit_regex = re.compile(r"\d+")

    # Check user input for presence of lower/upper case and digits.
    lower_case_detected = lower_case_regex.search(password)
    upper_case_detected = upper_case_regex.search(password)
    digit_detected = digit_regex.search(password)

    # Check if password is at least 8 characters long, has at least 1 upper
    # case, lower case and digit.
    if len(password) < 8:
        print("Password is weak. Must be at least 8 characters long.")
    elif None in (lower_case_detected, upper_case_detected, digit_detected):
        print("""Password is weak. Must have at least one lower case, upper
case and digit each.""")
    else:
        print("Password is strong. Satisfies all requirements.")


print("""\nFor a password to be considered strong, it must be at least 8
characters long. It should also have at least 1 lower case, upper case and
number.""")

password_input_1 = input("\nEnter your password: ").strip()

password_strength(password_input_1)
