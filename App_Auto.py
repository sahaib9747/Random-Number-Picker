# starting point
import random

number = random.randint(1, 1000)
attempts = 0
low = 1
high = 1000

while True:
    print("Guess the number (berween 1 and 1000)")
    input_number = (low + high) // 2  # only interger division
    print("My Guess is", input_number)
    attempts += 1
    if input_number == number:
        print("Yes,Your guess is correct!")
        break

    if input_number > number:
        print("Incorrect! Please try to guess a smaller number")
        high = input_number - 1
    else:
        print("Incorrect! Please try to guess a larger number")
        low = input_number + 1

print("You Tried", attempts, "Times to find the correct number")
