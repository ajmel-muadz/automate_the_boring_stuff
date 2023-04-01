# multiplication_quiz.py - A program that asks a number of multiplication
# questions with a timer and allows 3 tries. There are 10 questions for
# each quiz.

import random
import time
import sys

print("""\n----------------------------------------------------------------------
Attention! This quiz gives you a 10-second time-limit for each
question. If you exceed it, your attempt will be considered wrong.
Also, you get 3 tries for each question. Good luck!
----------------------------------------------------------------------""")

start_game = input("\nWould you like to start? (yes/no): ").lower().strip()
if start_game != "yes" and start_game != 'y':
    sys.exit()  # Exit quiz if user does not choose 'yes'/'y'

number_of_questions = 10  # Number of questions to be given
correct_answers = 0  # Used to display user score at the end of quiz

for question_number in range(number_of_questions):
    tries = 0
    num1 = random.randint(0, 24)
    num2 = random.randint(0, 24)

    while tries < 3:
        print(f"\n{question_number + 1}) What is {num1} x {num2}?")
        start = time.monotonic()
        response = int(input("Answer: "))
        end = time.monotonic()

        time_elapsed = end - start

        if time_elapsed > 10:
            print("Exceeded 10 second limit. No point awarded.")
            print(f"The correct answer is {num1 * num2}.")
            time.sleep(2)
            break

        if response == num1 * num2:
            print("Correct!")
            correct_answers += 1
            time.sleep(2)
            break

        elif response != num1 * num2:
            tries += 1
            if tries == 3:
                print("Incorrect. You reached 3 tries. No point awarded.")
                print(f"The correct answer is {num1 * num2}.")
                time.sleep(2)
                break

            print(f"Incorrect. Try again. You have {3 - tries} tries left.")
            time.sleep(2)
            continue

print(f"\nYour score is {correct_answers}/{number_of_questions}.")

# Personalised messages for a certain score out of 10.
if correct_answers == 0:
    print("You are possibly the dumbest person alive.")
elif 0 < correct_answers <= 3:
    print("You got a lot of practicing to do.")
elif 3 < correct_answers <= 6:
    print("Not bad I guess. Still can do better.")
elif 6 < correct_answers <= 8:
    print("That's quite good!")
elif correct_answers == 9:
    print("Almost had it! That's a wonderful mark.")
else:
    print("Perfection.")
