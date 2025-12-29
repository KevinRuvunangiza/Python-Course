print("WELCOME TO YOUR PASSWORD MANAGER")

default_password = 123

def set_new_password():
    global default_password
    default_password = int(input("Enter a New Password [NUMBERS ONLY]: "))
    print("Password updated!\n")

def test_password():
    test = int(input("Enter password to Test: "))
    if test == default_password:
        print("Password is Okay!\n")
    else:
        print("Password is Wrong!!!\n")

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
        print("Invalid option\n")
