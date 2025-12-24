import random

# Before this session when you launched a program it only executed once than you had to manually re-execute it
# Now we are going to talk about loops more precisely the [while] loop

# Like it's name sort of implies the loop runs until a certain condition is met.
# Think of it like in a video game an enemy will keep attacking as long as it's not dead.

secret_number = random.randint(1,10)

# while True: # This [while True] line will create what we call an infinite loop it will run sort of forever depending on the amount of RAM of your Pc
    
#     guess = int(input("Guess the number: "))
#     if guess == secret_number:
#         print("Congrats you found the number!!!")
#         break # The [break] keyword is used to exit out of a loop or later on a function
#     else:
#         print("Try again!")

# What this program wil do is pretty simple it will generate a random number store it
# Then our while loop will run indefinitely until you find the correct answer

# Simple counter

# This counter will keep decreasing until the condition is false in that case it will be until the [count] is less then or equal to zero
count = 10
while count >= 0:
    print(count)
    count-= 1
# NOTE: The [-=,+=] operators are the same equivalent as writing [a = a+1, a = a-1] it's a way for us to shorten it you can increment or decrement by the amount you want.

# Before tackling the next challenge I want you to make the previous code increment instead of decrement
    