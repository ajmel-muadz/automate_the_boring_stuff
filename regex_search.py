# regex_search.py - A program which opens all .txt files in a folder and
# searches for any line that matches a user-supplied regular expression.

from pathlib import Path
import os
import re

user_regex_input = input("Enter your regular expression: ")
regex = re.compile(user_regex_input)

for file in os.listdir(Path.home()/"Documents"/"Regex Search"):
    opened_file = open(Path.home()/"Documents"/"Regex Search"/file)
    file_content = opened_file.read()
    opened_file.close()

    regex_found = regex.findall(file_content)

    if regex_found != []:
        print(f"\nRegular expressions matched: {regex_found}")
    else:
        print(f"\nNo regular expressions matched with the term \
              '{user_regex_input}'.")
