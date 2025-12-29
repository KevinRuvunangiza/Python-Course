# As much as you might have loved your code before it was kind of spaghetti-like in this session I'll introduce to you functions/methods

# See functions as a way to write reusable code for now..later you'll see that they are more comparable to factories but forget it.
# In Python to write a [function] we use the keyword def.

def greet():
    print("Hello, Stranger!")

# I just created a [function] called 'greet' it will display a message every time it is 'called',to call a function we do as so:

greet() # That's it the function has been called

# Let me talk to you about the [return] keyword it does exactly what you think it makes our function return a certain value

# def check_password():
#     return True

# [print(check_password())] If I print the value of this function it will display [True] because I made the function do that

# Arguments
# Functions/Methods can take 'Inputs' in the for of arguments you've been using them since Day #1 with the [print("Everything here is an argument")]

def check_password(entered_password):
    correct_password = "12345"
    
    if entered_password != correct_password:
        return False
    else:
        return True
    
print(check_password("12345"))