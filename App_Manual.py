# starting point
import random

number = random.randint(1, 1000)
attempts = 0
while True:  # infinite loop
    input_number = input("Guess the number (berween 1 and 1000):")
    input_number = int(input_number)  # converting to intiger
    attempts += 1

    if input_number == number:
        print("Yes,Your guess is correct!")
        break  # finish the game if true

    if input_number > number:
        print("Incorrect! Please try to guess a smaller number")
    else:
        print("Incorrect! Please try to guess a larger number")

print("You Tried", attempts, "Times to find the correct number")
