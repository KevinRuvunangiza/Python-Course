import random

# I need you to add a live system so that the program stops when the player runs out of them
# Use everything you learned so far
# HAPPY CODING

secret_number = random.randint(1,10)

while True: # This [while True] line will create what we call an infinite loop it will run sort of forever depending on the amount of RAM of your Pc
    
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Congrats you found the number!!!")
        break # The [break] keyword is used to exit out of a loop or later on a function
    else:
        print("Try again!")