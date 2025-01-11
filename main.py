# Security+ Learning Tool
# Featuring: Professor Messer
# Created by: Nick Lueth
# Last updated: 1/11/2025

import webbrowser
import json
from InputIO import *
from random import randint

# Global dictionaries to store topics, links, and acronyms
topics = {}
links = {}
acronyms = {}  # Stores acronyms and their descriptions


def main():
    """
    Main entry point for the program. Loads the JSON data and displays the main menu.
    :return: None
    """
    load_json()
    main_menu()


def load_json():
    """
    Loads data from JSON files and populates the global dictionaries for topics, links, and acronyms.
    The JSON files contain data related to Security+ study topics and associated acronyms.

    :return: None
    """
    # List of topic files to load
    files = ["data/(1)GSC.json", "data/(2)TVM.json", "data/(3)SA.json", "data/(4)SO.json", "data/(5)SPMaO.json"]
    for file in files:
        with open(file) as json_file:
            json_data = json.load(json_file)
            file_name = file[8:-5]  # Extract the category from the filename
            topics[file_name] = json_data  # Add to the global 'topics' dictionary

    # Load links data
    with open("data/links.json") as link_file:
        link_data = json.load(link_file)
        for item in link_data.items():
            links[item[0]] = item[1]  # Add to the global 'links' dictionary

    # Load acronyms data
    with open("data/acronyms.json") as acronym_file:
        acronym_data = json.load(acronym_file)
        for acronym in acronym_data.items():
            acronyms[acronym[0]] = acronym[1]  # Add to the global 'acronyms' dictionary


def main_menu():
    """
    Displays the main menu and handles user input to navigate between study options, progress viewing,
    resetting progress, and saving/quit actions.

    :return: None
    """
    menu = ("Main menu:\n"
            "1. Study\n"
            "2. View Progress\n"
            "3. Reset Progress\n"
            "4. Save and Quit\n"
            "Choice: ")

    while True:
        clear()  # Clears the console screen
        choice = int_input_getter(menu, range(1, 5))  # Get valid input from user
        if choice == 1:
            study()
        elif choice == 2:
            view_progress()
        elif choice == 3:
            reset_manager()
        elif choice == 4:
            save()  # Save progress before exiting
            exit(0)  # Exit the program


def reset_manager():
    """
    Handles the resetting of user progress for specific topics or all topics.
    Allows the user to reset the progress of individual categories or all categories at once.

    :return: None
    """
    while True:
        clear()  # Clears the console screen
        menu = ("Which section would you like to reset?:\n"
                "1. All\n"
                "2. General Security Concepts\n"
                "3. Threats, Vulnerabilities, and Mitigations\n"
                "4. Security Architecture\n"
                "5. Security Operations\n"
                "6. Security Program Management and Oversight\n"
                "7. Acronyms\n"
                "b. Back\n")
        choice = int_input_getter(menu, range(1, 8))  # Get valid input from user
        if choice == 1:
            reset_all()  # Reset all categories
        elif choice == 2:
            reset("GSC")  # Reset General Security Concepts
        elif choice == 3:
            reset("TVM")  # Reset Threats, Vulnerabilities, and Mitigations
        elif choice == 4:
            reset("SA")  # Reset Security Architecture
        elif choice == 5:
            reset("SO")  # Reset Security Operations
        elif choice == 6:
            reset("SPMaO")  # Reset Security Program Management and Oversight
        elif choice == 7:
            reset_acronyms()  # Reset Acronym progress
        else:
            break  # Return to the main menu


def reset(category):
    """
    Resets the progress for a specific topic category.

    :param category: (str) The category to reset (e.g., 'GSC', 'TVM', 'SA', etc.)
    :return: None
    """
    categories = {"GSC": "General Security Concepts", "TVM": "Threats, Vulnerabilities, and Mitigations",
                  "SA": "Security Architecture", "SO": "Security Operations",
                  "SPMaO": "Security Program Management and Oversight"}

    print(f"ARE YOU SURE YOU WANT TO RESET YOUR '{categories[category]}' PROGRESS????")
    proceed = input('Type: "proceed"\nResponse: ').lower()
    if proceed == "proceed":
        # Reset progress for the selected category
        for topic in topics[category].items():
            if topic[1]:
                topics[category][topic[0]] = False
    else:
        clear()
        print("No changes were made.")
        input("Press enter to continue...")


def reset_acronyms():
    """
    Resets the user's progress for all acronyms.

    :return: None
    """
    print("ARE YOU SURE YOU WANT TO RESET YOUR 'Acronyms' PROGRESS???")
    proceed = input('Type: "proceed"\nResponse: ').lower()
    if proceed == "proceed":
        # Reset progress for all acronyms
        for key in acronyms.keys():
            if acronyms[key][2]:
                acronyms[key][2] = False
    else:
        clear()
        print("No changes were made.")
        input("Press enter to continue...")


def reset_all():
    """
    Resets the progress for all categories and acronyms.

    :return: None
    """
    print("ARE YOU SURE YOU WANT TO RESET ALL OF YOUR PROGRESS???")
    proceed = input('Type: "proceed"\nResponse: ').lower()
    if proceed == "proceed":
        categories = ['GSC', 'TVM', 'SA', 'SO', 'SPMaO']
        # Reset progress for all categories
        for category in categories:
            for topic in topics[category].items():
                if topic[1]:
                    topics[category][topic[0]] = False
        # Reset progress for all acronyms
        for key in acronyms.keys():
            if acronyms[key][2]:
                acronyms[key][2] = False
    else:
        clear()
        print("No changes were made.")
        input("Press enter to continue...")


def study():
    """
    Displays the study menu and allows the user to study different categories or acronyms.
    Also shows the user's progress for each domain.

    :return: None
    """
    while True:
        category_menu = (f"Categories:\n"
                         f"1. General Security Concepts ({get_progress(topics['GSC'])}%)\n"
                         f"2. Threats, Vulnerabilities, and Mitigations ({get_progress(topics['TVM'])}%)\n"
                         f"3. Security Architecture ({get_progress(topics['SA'])}%)\n"
                         f"4. Security Operations ({get_progress(topics['SO'])}%)\n"
                         f"5. Security Program Management and Oversight ({get_progress(topics['SPMaO'])}%)\n"
                         f"6. Acronyms ({get_progress(acronyms)}%)\n"
                         f"B. Back\n"
                         f"Choice: ")

        clear()
        category_choice = int_input_getter(category_menu, range(1, 7))  # Get valid input from user
        if category_choice == 1:
            display_topics(topics["GSC"], "GSC")  # General Security Concepts
        elif category_choice == 2:
            display_topics(topics["TVM"], "TVM")  # Threats, Vulnerabilities, and Mitigations
        elif category_choice == 3:
            display_topics(topics["SA"], "SA")  # Security Architecture
        elif category_choice == 4:
            display_topics(topics["SO"], "SO")  # Security Operations
        elif category_choice == 5:
            display_topics(topics["SPMaO"], "SPMaO")  # Security Program Management and Oversight
        elif category_choice == 6:
            acronym_menu()
        else:
            break  # Return to the main menu


def acronym_menu():
    """
    Displays the acronym menu and provides options to study random acronyms or select from a list.

    :return: None
    """
    menu = ("How would you like to study acronyms?:\n"
            "1. Study random acronym\n"
            "2. Select from list\n"
            "B. Back\n")

    while True:
        clear()
        choice = int_input_getter(menu, range(1, 3))  # Get valid input from user
        if choice == 1:
            get_random_acronym()  # Study a random acronym
        elif choice == 2:
            display_acronyms()  # Display a list of acronyms
        else:
            break  # Return to the study menu


def get_random_acronym():
    """
    Selects an unlearned acronym at random for the user to study.

    :return: None
    """
    unlearned_acronyms = get_unlearned_acronyms()  # Get a list of unlearned acronyms
    solve_acronym(unlearned_acronyms[randint(0, len(unlearned_acronyms) - 1)])


def get_unlearned_acronyms():
    """
    Returns a list of acronyms that have not been learned yet (i.e., progress is not marked as True).

    :return: list of unlearned acronyms
    """
    unlearned_acronyms = [key for key, value in acronyms.items() if not value[2]]
    return unlearned_acronyms


def display_acronyms():
    """
    Displays a list of all acronyms available for study, showing whether each one is completed or not.

    :return: None
    """
    new_menu = ""
    keys = list(acronyms.keys())
    clear()
    print("Acronyms:")
    for i, (acronym, data) in enumerate(acronyms.items()):
        new_menu += f"{i + 1}. {'[X]' if data[2] else '[ ]'} {acronym} - {data[1]} \n"
    new_menu += "B. Back \nChoice: "
    response = int_input_getter(new_menu, range(1, len(acronyms) + 1))  # Get valid input from user
    if response == 0:
        return
    else:
        solve_acronym(keys[response - 1])  # Let the user solve the selected acronym


def solve_acronym(acronym):
    """
    Prompts the user to solve an acronym by typing the correct meaning. Marks it as complete if the answer is correct.

    :param acronym: (string) The acronym to solve
    :return: None
    """
    clear()
    print(f"What does {acronym} stand for?\nHint: {acronyms[acronym][1]}")
    answer = input("Answer: ")
    if answer.lower() == acronyms[acronym][0].lower():  # Check if the answer matches
        acronyms[acronym][2] = True  # Mark as completed
        print("Correct!")
    else:
        print(f"\nSorry, the correct answer was: {acronyms[acronym][0]}")
        wrong = yes_or_no_handler("\nWould you like to mark that acronym as complete?(y/n): ")
        if wrong == "y":
            acronyms[acronym][2] = True  # Mark as completed if user wants


def display_topics(topic_dict, cat_name):
    """
    Displays a list of topics for the selected category, showing their completion status.

    :param topic_dict: (dict) The dictionary of topics to display
    :param cat_name: (str) The category name
    :return: None
    """
    new_menu = ""
    keys = list(topic_dict.keys())
    clear()
    titles = {
        "GSC": "General Security Concepts",
        "TVM": "Threats, Vulnerabilities, and Mitigations",
        "SA": "Security Architecture",
        "SO": "Security Operations",
        "SPMaO": "Security Program Management and Oversight"
    }
    print(titles[cat_name] + ":")
    for i, (topic, completed) in enumerate(topic_dict.items()):
        new_menu += f"{i + 1}. {'[X]' if completed else '[ ]'} {topic} \n"
    new_menu += "B. Back \nChoice: "
    response = int_input_getter(new_menu, range(1, len(topic_dict) + 1))  # Get valid input from user
    if response == 0:
        return
    else:
        webbrowser.open(links[keys[response - 1]])  # Open the link for the selected topic
        mark_complete = yes_or_no_handler("Would you like to mark that topic complete?(y/n): ")
        if mark_complete == "y":
            topic_dict[keys[response - 1]] = True  # Mark the topic as complete


def view_progress():
    """
    Displays the user's progress in each topic category and acronyms. Shows a summary of completion percentages.

    :return: None
    """
    clear()
    total_topics = 0.0
    num_completed = 0
    cats = ['GSC', 'TVM', 'SA', 'SO', 'SPMaO']
    for cat in cats:
        total_topics += float(get_progress(topics[cat]))  # Add progress of each category
    for acronym in acronyms.values():
        if acronym[2]:  # If acronym is marked as completed
            num_completed += 1
    overall_progress = ((num_completed / 321 * 100) + total_topics) / 6  # Calculate overall progress

    if overall_progress == 100.00:
        print("CONGRATULATIONS! YOU'RE READY TO TAKE YOUR TEST!")

    print(f"Progress Report:\n"
          f"General Security Concepts ({get_progress(topics['GSC'])}%)\n"
          f"Threats, Vulnerabilities, and Mitigations ({get_progress(topics['TVM'])}%)\n"
          f"Security Architecture ({get_progress(topics['SA'])}%)\n"
          f"Security Operations ({get_progress(topics['SO'])}%)\n"
          f"Security Program Management and Oversight ({get_progress(topics['SPMaO'])}%)\n"
          f"Acronyms ({get_progress(acronyms)}%)\n"
          f"TOTAL: {overall_progress:.2f}%\n")
    input("Press enter to continue...")


def get_progress(topic_dict):
    """
    Calculates and returns the completion percentage for a given topic dictionary.

    :param topic_dict: (dict) The dictionary containing topics or acronyms
    :return: (float) A string representing the completion percentage (e.g., '80.00')
    """
    dict_len = len(topic_dict)
    num_completed = 0
    if isinstance(list(topic_dict.values())[0], bool):  # Topics are boolean (completed/incomplete)
        for topic in topic_dict.values():
            if topic:
                num_completed += 1
        return f"{(num_completed / dict_len) * 100:.2f}"
    else:  # Acronyms are lists with the third element indicating completion status
        for topic in topic_dict.values():
            if topic[2]:
                num_completed += 1
        return f"{(num_completed / dict_len) * 100:.2f}"


def save():
    """
    Saves the current progress of topics and acronyms back to their respective JSON files.

    :return: None
    """
    # Save topics
    files = ["data/(1)GSC.json", "data/(2)TVM.json", "data/(3)SA.json", "data/(4)SO.json", "data/(5)SPMaO.json"]
    for file in files:
        with open(file, "w") as json_file:
            json.dump(topics[file[8:-5]], json_file, indent=4)

    # Save acronyms
    with open("data/acronyms.json", "w") as acronym_file:
        json.dump(acronyms, acronym_file, indent=4)


if __name__ == '__main__':
    main()
