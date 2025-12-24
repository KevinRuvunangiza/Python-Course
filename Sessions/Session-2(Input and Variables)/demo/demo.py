
# VARIABLES

# You can think of variables as labeled boxes in which you can store your data,they are used everywhere
# They are there to make your life as a dev easier because they allow us to give names to data and on top of that they make that data reusable
#To declare a variable in python you need 2 things a NAME and a VALUE

# In this case [user_name] is the variable name and ["Kevin"] is the value,the name of the variable is always on the left
# Let's talk about data types, data types or types it's just what the variable is or what it might be
 
user_name = "Kevin" # String
age = 20 # Integer
balance = 20.01 # Float
isAlive = True # Boolean

# INPUT

# Input is what makes coding fun at least for me, up until now the we were the ones listening to the computer but now we will make him
# Listen to us.
# To do so in python we will use another built-in function called [input()].
# When the function is called our program will display whatever is between the parentheses and wait for an input/answer from us

#input("What's your name: ")

# For now our [input()] is useless because our answer isn't being stored anywhere to change that let's store the question in a variable
# While we are there let's print it too

name = input("What's your name: ")
print(f"Welcome {name}")
