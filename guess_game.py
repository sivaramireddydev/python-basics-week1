#📌 Goal:
#User guesses a number between 1 to 10
#Computer compares it to a random number
#Tells if it’s correct or not

import random

target = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == target:
    print("🎉 Correct! You guessed the number!")
else:
    print(f"❌ Wrong! The correct number was {target}")
