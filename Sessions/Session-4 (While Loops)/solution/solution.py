import random

secret_number = random.randint(1, 10)
lives = 3

while lives > 0:
    print(f"Lives remaining: {lives}")
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("You Won!")
        break # Exit the loop immediately
    else:
        print("Wrong!")
        lives-= 1 # Decrease life

if lives == 0:
    print("Game Over. You ran out of lives.")