import time # This is a library we will talk about it later but just know that it allows us to add some extra functionalities to our code

# Goal: Learn about the [print()] function and get familiar with the terminal/console

# Demo v1

# You can put whatever you want between the [()] of the [print()] it can take any value 
# Text(string),Whole Numbers(integer or int),Decimal Numbers(floats,long,short,etc...), Boolean(True or False) and many more... Those are called data types
# Note: The computer will only recognize a letter or a sentence as a string if it's between [""].

print("--- Initializing protocol ---")
print("--- SYSTEM BOOTED SUCCESSFULLY")
print("Hello World!")

print("\n") # The symbol [\n] is interpreted by the computer as a new line whenever he sees it he knows that he has to skip/add an empty line

# Demo v2

print("--- Initializing protocol ---")
time.sleep(1)
print("--- SYSTEM BOOTED SUCCESSFULLY")
time.sleep(1)
print("Hello World!")

