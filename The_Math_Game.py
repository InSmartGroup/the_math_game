import random
import sys

score = 0


def addition():
    global score
    while True:
        number_1 = random.randint(1, 50)
        number_2 = random.randint(1, 50)
        print()
        print(f"{number_1} + {number_2} = ?")
        answer = input()
        if answer == 'quit':
            print("Thank you for playing.")
            print(f"Your final score is {score}.")
            break
        if answer.isalpha():
            print("Please use digits to type answers.")
            continue
        if int(answer) == number_1 + number_2:
            print("Correct!")
            score += 1
            print(f"Your score: {score} points.")
            continue
        elif int(answer) != number_1 + number_2:
            print("Wrong!")
            print(f"The answer is {number_1 + number_2}.")
            score -= 1
            if score < 0:
                score = 0
            print(f"Your score: {score} points.")
            continue


def subtraction():
    global score
    while True:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        if number_2 > number_1:
            number_2 = random.randint(1, 100)
            continue
        print()
        print(f"{number_1} - {number_2} = ?")
        answer = input()
        if answer == 'quit':
            print("Thank you for playing.")
            print(f"Your final score is {score}.")
            break
        if answer.isalpha():
            print("Please use digits to type answers.")
            continue
        if int(answer) == number_1 - number_2:
            print("Correct!")
            score += 1
            print(f"Your score: {score} points.")
            continue
        elif int(answer) != number_1 - number_2:
            print("Wrong!")
            print(f"The answer is {number_1 - number_2}.")
            score -= 1
            if score < 0:
                score = 0
            print(f"Your score: {score} points.")
            continue


def multiplication():
    global score
    while True:
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 10)
        if number_1 == 1 or number_2 == 1:
            number_1 = random.randint(1, 10)
            number_2 = random.randint(1, 10)
            continue
        print()
        print(f"{number_1} * {number_2} = ?")
        answer = input()
        if answer == 'quit':
            print("Thank you for playing.")
            print(f"Your final score is {score}.")
            break
        if answer.isalpha():
            print("Please use digits to type answers.")
            continue
        if int(answer) == number_1 * number_2:
            print("Correct!")
            score += 1
            print(f"Your score: {score} points.")
            continue
        elif int(answer) != number_1 * number_2:
            print("Wrong!")
            print(f"The answer is {number_1 * number_2}.")
            score -= 1
            if score < 0:
                score = 0
            print(f"Your score: {score} points.")
            continue


def division():
    global score
    while True:
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 10)
        if number_2 > number_1:
            number_2 = random.randint(1, 10)
            continue
        print()
        print(f"{number_1 * number_2} / {number_2} = ?")
        answer = input()
        if answer == 'quit':
            print("Thank you for playing.")
            print(f"Your final score is {score}.")
            break
        if answer.isalpha():
            print("Please use digits to type answers.")
            continue
        if int(answer) == ((number_1 * number_2) / number_2):
            print("Correct!")
            score += 1
            print(f"Your score: {score} points.")
            continue
        elif int(answer) != ((number_1 * number_2) / number_2):
            print("Wrong!")
            print(f"The answer is {(number_1 * number_2) / number_2}.")
            score -= 1
            if score < 0:
                score = 0
            print(f"Your score: {score} points.")
            continue


def game():
    print("WELCOME TO THE MATH GAME!")
    while True:
        print("Type (a)ddition, (s)ubtraction, (m)ultiplication, (d)ivision")
        print("Type 'quit' to quit the game.")
        selection = input().lower()
        if selection == 'quit':
            print("Exiting the program.")
            sys.exit()
        if selection == 'a':
            addition()
            break
        elif selection == 's':
            subtraction()
            break
        elif selection == 'm':
            multiplication()
            break
        elif selection == 'd':
            division()
        else:
            print("Please type 'a' for addition, 's' for subtraction, 'm' for multiplication, 'd' for division.")
            continue


game()
