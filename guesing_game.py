# generate a number between 1 and 10 and ask the user to guess it until they get it right
import random

number_to_guess = random.randint(1, 10)

while True :
            guess = int(input("Guess a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                print("Please guess a number within the range of 1 to 10.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print("Congratulations! You've guessed the right number!")