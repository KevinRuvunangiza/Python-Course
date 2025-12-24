# CONDITIONALS

# So we saw that we could take an input using [input()] but the thing is that if the user didn't play along he would sort of break our program
# To be able to prevent such things from happening we will learn about conditions,they help us control the flow of our program and make it more flexible/smart
# Conditions in python are written using the keyword [if]

age = int(input("Enter your age: "))
has_permission = True

# if age>=18: # Checks if the age is greater or equal to 18
#     print("You are an adult") # If it's the case whatever is here will execute
# else: # If the age doesn't fulfill the condition
#     print("You are too young") # This code will execute

# Let's talk comparators they work the same as the ones you saw in primary school we use [>,<,==,=<,=>]
# NOTE: In most programming languages we use [==] to check equality because [=] is reserved for assigning values and [!=] means isn't equal in programming every time you'll see [!] it just means NOT

# We can make way more complex conditions
# CONTEXT: In the USA you are an adult at 18 but you are legally allowed to drink at 21 so let's create a condition that includes that

# [AND] Operator

# if age>=18 and age>=21:
#     print("You are an adult and can drink")
# elif age>=18 and age<21:
#     print("You are an adult but can't drink")
# else:
#     print("You are too young")
    
# OR Operator

if age>=18 or has_permission==True:
    print("You can go out")
else:
    print("Better listen to your parent")

# NOTE: [OR] and [AND] are called [LOGICAL OPERATORS] there job is pretty straight forward
# When using [AND] both conditions has to be True for your code to execute
# When using [OR] only one condition needs to be true for your code to be executed

# Talk about indentation in private