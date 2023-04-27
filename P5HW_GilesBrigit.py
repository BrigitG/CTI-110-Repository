# The project is a simple math quiz program where the user can choose to add or subtract random numbers and receive feedback on the correctness of their answers.

# 4/27/2023

# CTI-110 P5HW - Math Quiz

# Brigit Giles

import random

print("Welcome to Math Quiz\n")

while True:
    print("MAIN MENU")
    print("-------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit\n")
    choice = input("Please choose one of the menu options: ")

    if choice == '1':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        answer = num1 + num2
        guess_count = 0
        while True:
            user_input = int(input(f"\nWhat is {num1} + {num2}? "))
            guess_count += 1
            if user_input == answer:
                print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {guess_count}\n")
                break
            elif user_input > answer:
                print("Sorry, guess is too high. Please try again.")
            else:
                print("Sorry, guess is too low. Please try again.")

    elif choice == '2':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        answer = num1 - num2
        guess_count = 0
        while True:
            user_input = int(input(f"\nWhat is {num1} - {num2}? "))
            guess_count += 1
            if user_input == answer:
                print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {guess_count}\n")
                break
            elif user_input > answer:
                print("Sorry, guess is too high. Please try again.")
            else:
                print("Sorry, guess is too low. Please try again.")

    elif choice == '3':
        print("Thank you for playing...\n Bye!!!\n")
        break

    else:
        print("Invalid choice. Please try again.\n")
