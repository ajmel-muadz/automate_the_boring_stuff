# sandwich_maker.py - A program that asks users for their sandwich
# preferences and displays the total cost of the ingredients using the
# PyInputPlus module.

import pyinputplus as pyip

price = {"wheat": 3, "white": 3.50, "sourdough": 4, "chicken": 2, "turkey": 4,
         "ham": 3, "tofu": 1, "cheddar": 1, "swiss": 2.50, "mozzarella": 2,
         "mayonnaise": 1, "mustard": 1, "lettuce": 1.50, "tomato": 1.25}

print("\nWelcome to the sandwich maker! Choose your sandwich below.")

# User prompted to choose bread type. Cannot be left blank or have wrong input.
bread_type = pyip.inputMenu(
    ["wheat", "white", "sourdough"], prompt="\nBread type:\n")
print(f"\nYou chose {bread_type}. Price is ${price[bread_type]}")

# User prompted to choose protein type. Cannot be left blank or have wrong 
# input.
protein_type = pyip.inputMenu(
    ["chicken", "turkey", "ham", "tofu"], prompt="\nProtein type:\n")
print(f"\nYou chose {protein_type}. Price is ${price[protein_type]}")

# User has the option of either having cheese or not.
cheese_option = pyip.inputYesNo("\nWould you like cheese? (yes/no):\n")

# If user chooses "yes", they have 3 varieties of cheeses to choose from.
if cheese_option == "yes":
    cheese_type = pyip.inputMenu(
        ["cheddar", "swiss", "mozzarella"], prompt="\nCheese type:\n")
    print(f"\nYou chose {cheese_type}. Price is ${price[cheese_type]}")

# 4 yes/no questions for condiments given to the user to choose from.
mayo_option = pyip.inputYesNo("\nWould you like mayonnaise? (yes/no):\n")
if mayo_option == "yes":
    print(f"\nMayonnaise is ${price['mayonnaise']}")
else:
    pass

mustard_option = pyip.inputYesNo("\nWould you like mustard? (yes/no):\n")
if mustard_option == "yes":
    print(f"\nMustard is ${price['mustard']}")
else:
    pass

lettuce_option = pyip.inputYesNo("\nWould you like lettuce? (yes/no):\n")
if lettuce_option == "yes":
    print(f"\nLettuce is ${price['lettuce']}")
else:
    pass

tomato_option = pyip.inputYesNo("\nWould you like tomatoes? (yes/no):\n")
if tomato_option == "yes":
    print(f"\nTomato is ${price['tomato']}")
else:
    pass

# User can choose how many sandwiches they want.
sandwich_number = pyip.inputInt(
    "\nHow many sandwiches would you like? : ", min=1)

total_price = sandwich_number * (price[bread_type] + price[protein_type] +
                                 price[cheese_type]
                                 + price['mayonnaise'] + price['mustard'] +
                                 price['lettuce'] +
                                 price['tomato'])

print(f"${total_price}")
