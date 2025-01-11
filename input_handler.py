from os import system, name


def clear():
    """
    Clears the terminal screen depending on the operating system.

    On Windows systems, it uses the 'cls' command.
    On Unix-based systems (Linux/macOS), it uses the 'clear' command.

    :return: None
    """
    if name == "nt":  # If running on a Windows system
        _ = system("cls")
    else:  # If running on a Unix-based system (e.g., Linux or macOS)
        _ = system("clear")


def yes_or_no_handler(prompt):
    """
    Prompts the user with a yes/no question and validates the input.
    Loops until a valid response ('y' or 'n') is provided.

    :param prompt: (str) The question or prompt to display to the user.
    :return: (str) 'y' for yes or 'n' for no based on the user's input.
    """
    while True:
        choice = input(prompt).lower()
        if choice == "y" or choice == "n":
            return choice  # Return the valid response
        else:
            print(f"{choice} is not a valid input. Please enter 'y' for yes or 'n' for no.")
            input("Press enter to continue...")
            clear()  # Clear the screen before asking again


def int_input_getter(prompt, num_range):
    """
    Prompts the user to choose an integer within a specific range, and ensures the input is valid.

    Continuously asks the user for a valid selection until the input is an integer within the provided range.
    The user can also enter 'b' to go back (represented by returning 0).

    :param prompt: (str) The prompt to display to the user.
    :param num_range: (range) The valid range of integers the user can select from.
    :return: (int) The user's choice, or 0 if 'b' is entered to go back.
    """
    while True:
        try:
            choice = input(prompt)  # Get user input
            if choice.lower() == "b":  # If user chooses to go back
                return 0
            else:
                choice = int(choice)  # Try to convert input to an integer
        except ValueError:
            # If the user enters something that's not an integer
            print("Please choose a valid number!")
            input("Press enter to continue...")
            clear()  # Clear the screen before re-asking
        else:
            # Check if the entered integer is within the valid range
            if choice in num_range:
                return choice  # Return the valid choice
            else:
                print("That is not a valid option!")
                input("Press enter to continue...")
                clear()  # Clear the screen before re-asking
