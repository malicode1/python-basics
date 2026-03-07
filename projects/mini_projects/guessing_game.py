# guessing_game
import random

print("---Guessing Game---")

secret_number = random.randint(1, 10)
guess_limit = 3

for i in range(guess_limit):
    guess = int(input("Guess the number between 1 and 10: "))
    if guess < secret_number:
        print("please enter bigger number")
        continue
    if guess > secret_number:
        print("please enter smaller number")
        continue
    if guess == secret_number:
        print(f"YOU WON! You found it in {i+1} tries.")
        break
else:
    print(f"YOU LOSE! The number was {secret_number}")