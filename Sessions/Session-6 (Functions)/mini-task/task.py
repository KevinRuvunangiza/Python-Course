
# Use everything you learned to create a menu that will allow a user to save a password
# No need to use libraries yet you can just keep the password during runtime 
# Each Action should use a function
# HINT: You might need the [global] keyword

default_password = 123

while True:
    user_input = int(input(
        "\n1. Set a New Password"
        "\n2. Test Password"
        "\n3. Check Current Password"
        "\n4. Exit\n"
    ))

    if user_input == 1:
        set_new_password()
    elif user_input == 2:
        test_password()
    elif user_input == 3:
        print("Current password is:", default_password)
    elif user_input == 4:
        break
    else:
        print("Invalid option")