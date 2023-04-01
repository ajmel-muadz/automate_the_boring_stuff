# madlibs.py - A python madlibs program.

from pathlib import Path
import re

text_file = open(Path.home()/"Documents"/"MadLibs.txt")
text = text_file.read()
text_file.close()

split_text = re.findall(r"[\w]+|[^\s\w]", text)

changed_split_text_list = []

for item in split_text:
    if item == "ADJECTIVE":
        adjective_input = input("Enter an adjective: ").strip()
        changed_split_text_list.append(adjective_input)
    elif item == "NOUN":
        noun_input = input("Enter a noun: ").strip()
        changed_split_text_list.append(noun_input)
    elif item == "ADVERB":
        adverb_input = input("Enter an adverb: ").strip()
        changed_split_text_list.append(adverb_input)
    elif item == "VERB":
        verb_input = input("Enter a verb: ").strip()
        changed_split_text_list.append(verb_input)
    else:
        changed_split_text_list.append(item)

changed_split_text = " ".join(changed_split_text_list)

final_text = changed_split_text.replace(' .', '.').replace(' ,', ',').\
    replace(' ?', '?').replace(' !', '!')
print(final_text)

complete_text_file = open(Path.home()/"Documents"/"NewMadLibs.txt", 'w')
final_text_file = complete_text_file.write(final_text)
complete_text_file.close()
