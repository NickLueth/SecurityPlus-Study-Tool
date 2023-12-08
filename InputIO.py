from os import system, name


def clear():
    """
    This function produces a terminal clear dependent on which operating system you are using.
    """
    # If you are using a Windows system
    if name == "nt":
        _ = system("cls")
    # If you are using a unix-based system
    else:
        _ = system("clear")


def yes_or_no_handler(prompt):
    while True:
        choice = input(prompt)
        if choice.lower() == 'y' or choice.lower() == 'n':
            return choice
        else:
            print(f"{choice} is not y or n")
            input("Press enter to continue...")
            clear()


def int_input_getter(prompt, num_range):
    """
    This function takes a prompt and displays it until the user chooses a valid option.
    :param prompt: (string) Prompt for user selection
    :param num_range: (range) Range of integer values that are available
    :return: choice (int) The user's selection
    """
    while True:
        try:
            choice = int(input(prompt))
        # If there is a value error pass so the loop can restart.
        except ValueError:
            print("Please choose a valid number!")
            input("Press enter to continue...")
            clear()
        # Otherwise, test to see if the number chosen is available.
        else:
            # If the number is available then return that number.
            if choice in num_range:
                return choice
            else:
                print("That is not an option!")
                input("Press enter to continue...")
                clear()
