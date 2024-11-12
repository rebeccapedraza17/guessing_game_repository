# Rebecca Pedraza
# Guessing game

# Imports
import random

# The computer will generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Guessing game!")
print("The computer is thinking of a random number between 1 and 100")

# Loop of the code
while True:
    guess = int(input("Enter your guess: "))

# Check for guesses
    if guess < secret_number:
        print("Guess again, your guess is low")
    elif guess > secret_number:
        print("Guess again, your guess is high")
    else:
        print("You guessed the correct number!")
        
        
