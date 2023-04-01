# regex_strip.py - Program that behaves very similarly to Python's
# in-built strip() function.

import re

user_input = input("\nEnter string: ")
argument_input = input("Enter argument to remove character (Enter to skip): ")

# Regex that finds trailing beginning and ending spaces.
space_regex = re.compile(r"^\s+|\s+$")
space_detected = space_regex.search(user_input)


def regex_strip(user_input, argument_input):
    if argument_input == "":
        space_regex = re.compile(r"^\s+|\s+$")
        space_detected = space_regex.search(user_input)

        if space_detected is not None:
            no_space = user_input.replace(space_detected.group(), "")
            print(no_space)
        else:
            print(user_input)
    else:
        character_regex = re.compile(r".")
        characters_detected = character_regex.findall(user_input)

        final_word = []
        for character in characters_detected:
            if character in argument_input:
                x = character.replace(character, "")
                final_word.append(x)
            else:
                final_word.append(character)

        for i in final_word:
            print(i, end='')


regex_strip(user_input, argument_input)
