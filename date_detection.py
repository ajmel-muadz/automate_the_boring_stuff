# date_detection.py - A program that utilises regular expressions to
# see if a date entered is correct.

import re

# Try to catch any AttributeError arising when any string input does
# not match date format specified in regular expression.
try:
    def valid():
        return "Valid. Date obeys all rules."

    user_input = input(
        "\nEnter date (Must follow DD/MM/YYYY format): ").strip()

    months_31_days = ["01", "03", "05", "07", "08", "10", "12"]
    months_30_days = ["04", "06", "09", "11"]

    # Regular expression that only matches dates with the format: DD/MM/YY.
    date_detection_regex = re.compile(r"^(\d?\d)/(\d?\d)/(\d?\d?\d?\d)$")
    date_detected = date_detection_regex.search(user_input)

    # Compartmentalise days, months and years in the date for future
    # calculations or format checking.
    date_day, date_month, date_year = date_detected.groups()

    # Days or months with only one digit will have a trailing '0' added.
    if len(date_day) < 2:
        date_day = '0' + date_day
    if len(date_month) < 2:
        date_month = '0' + date_month
    if len(date_year) < 4:
        date_year = (4 - len(date_year)) * '0' + date_year

    # Day range allowed is 01-31 for months with a maximum of 31 days.
    if date_month in months_31_days:
        if int(date_day) > 31:
            print("Invalid. Month given has a maximum of 31 days.")
        else:
            print(valid())

    # Day range allowed is 01-30 for months with a maximum of 30 days.
    elif date_month in months_30_days:
        if int(date_day) > 30:
            print("Invalid. Month given has a maximum of 30 days.")
        else:
            print(valid())

    # Day range allowed for February is dependent on a few rules.
    elif date_month == "02":
        # Any non-century year divisible by 4 is a leap year.
        if int(date_year) % 4 == 0 and int(date_year) % 100 != 0:
            if int(date_day) > 29:
                print("Invalid. Leap year has a maximum of 29 days for \
February.")
            else:
                print(valid())
        # Any century year has to be divisible by both 100 and 400 to be a
        # leap year.
        elif int(date_year) % 100 == 0 and int(date_year) % 400 == 0:
            if int(date_day) > 29:
                print("Invalid. Leap year has a maximum of 29 days for \
February.")
            else:
                print(valid())
        # Years that do not obey the aforementioned rules are not leap years
        # so have a maximum of 28 days.
        else:
            if int(date_day) > 28:
                print("Invalid. A non-leap year February has a maximum of \
28 days.")
            else:
                print(valid())

# Catches any error so program tells user date format is not correct, instead
# of crashing program.
except AttributeError:
    print("Format does not follow DD/MM/YYYY. Please enter a date.")
