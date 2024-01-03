# Security+ Learning Tool
# Featuring: Professor Messer
# Created by: Nick Lueth
# Last updated: 1/2/2023


import webbrowser
import json
from InputIO import *
from random import randint


topics = {}
links = {}
acronyms = {}  # Load acronyms


def main():
    load_json()
    main_menu()


def load_json():
    """
    This function loads the JSON data in the topics and links global dictionaries.
    :return: None
    """
    files = ["data/(1)GSC.json", "data/(2)TVM.json", "data/(3)SA.json", "data/(4)SO.json", "data/(5)SPMaO.json"]
    for file in files:
        with open(file) as json_file:
            json_data = json.load(json_file)
            file_name = file[8:-5]
            topics[file_name] = json_data
    with open("data/links.json") as link_file:
        link_data = json.load(link_file)
        for item in link_data.items():
            links[item[0]] = item[1]
    with open("data/acronyms.json") as acronym_file:
        acronym_data = json.load(acronym_file)
        for acronym in acronym_data.items():
            acronyms[acronym[0]] = acronym[1]


def main_menu():
    """
    This function displays the main menu and defines what code to execute based on the user's selection.
    :return: None
    """
    menu = """Main menu:
1. Study
2. View Progress
3. Reset Progress
4. Save and Quit
Choice: """
    while True:
        clear()
        choice = int_input_getter(menu, range(1, 5))
        if choice == 1:
            study()
        elif choice == 2:
            view_progress()
        elif choice == 3:
            reset()
        elif choice == 4:
            save()
            exit(0)


def reset():
    """
    This function resets the progress of the user.
    :return: None
    """
    clear()
    print("ARE YOU SURE YOU WANT TO RESET YOUR PROGRESS????")
    proceed = input('Type: "proceed"\nResponse: ').lower()
    if proceed.__eq__("proceed"):
        cats = ['GSC', 'TVM', 'SA', 'SO', 'SPMaO']
        for cat in cats:
            for topic in topics[cat].items():
                if topic[1]:
                    topics[cat][topic[0]] = False
        for key in acronyms.keys():
            if acronyms[key][2]:
                acronyms[key][2] = False
        save()
    else:
        clear()
        print("No changes were made.")
        input("Press enter to continue...")


def study():
    """
    This function displays the study menu and defines what code to execute based on the user's selection. It also
    displays the user's progress in each domain.
    :return: None
    """
    while True:
        category_menu = f"""Categories:
1. General Security Concepts ({get_progress(topics["GSC"])}%)
2. Threats, Vulnerabilities, and Mitigations ({get_progress(topics["TVM"])}%)
3. Security Architecture ({get_progress(topics["SA"])}%)
4. Security Operations ({get_progress(topics["SO"])}%)
5. Security Program Management and Oversight ({get_progress(topics["SPMaO"])}%)
6. Acronyms ({get_progress(acronyms)}%)
7. Back
Choice: """
        clear()
        category_choice = int_input_getter(category_menu, range(1, 8))
        if category_choice == 1:
            display_topics(topics["GSC"], "GSC")
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
            break


def acronym_menu():
    """
    This function manages the acronym menu options.
    :return: None
    """
    menu = """How would you like to study acronyms?:
1. Study random acronym
2. Select from list
3. Back
"""
    while True:
        clear()
        choice = int_input_getter(menu, range(1, 4))
        if choice == 1:
            get_random_acronym()
        elif choice == 2:
            display_acronyms()
        else:
            break


def get_random_acronym():
    """
    This function selects an unlearned acronym at random to study.
    :return: None
    """
    unlearned_acronyms = get_unlearned_acronyms()
    solve_acronym(unlearned_acronyms[randint(0, len(unlearned_acronyms))])


def get_unlearned_acronyms():
    """
    This function makes the list of unlearned acronyms.
    :return: unlearned_acronyms (list) a list of unlearned acronyms
    """
    unlearned_acronyms = []
    for acronym in acronyms.items():
        if not acronym[1][2]:
            unlearned_acronyms.append(acronym[0])
    return unlearned_acronyms


def display_acronyms():
    """
    This function displays a list of all acronyms to study.
    :return: None
    """
    new_menu = """"""
    keys = list(acronyms.keys())
    clear()
    last_index = 0
    for i, topic in enumerate(acronyms.items()):
        new_menu += f"{i + 1}. {'[X]' if topic[1][2] else '[ ]'} {topic[0]} - {topic[1][1]} \n"
        last_index = i + 1
    new_menu += f"{last_index + 1}. Back \nChoice: "
    response = int_input_getter(new_menu, range(1, last_index + 2))
    if response == last_index + 1:
        return
    else:
        solve_acronym(keys[response - 1])


def solve_acronym(acronym):
    """
    This function manages solving an acronym.
    :param acronym: (string) The acronym key
    :return: None
    """
    clear()
    print(f"What does {acronym} stand for?\nHint: {acronyms[acronym][1]}")
    answer = input("Answer: ")
    if answer.lower().__eq__(acronyms[acronym][0].lower()):
        acronyms[acronym][2] = True
        print("Correct!")
        input("Press enter to continue...")
    else:
        print(f"\nSorry, the correct answer was:\n{acronyms[acronym][0]}")
        wrong = yes_or_no_handler("\nWould you like to mark that acronym as complete?(y/n): ")
        if wrong.__eq__("y"):
            acronyms[acronym][2] = True


def display_topics(topic_dict, cat_name):
    """
    This function displays the topics in a selected domain.
    :param topic_dict: (dict) The dictionary of topics
    :param cat_name: (str) The name of the category
    :return: None
    """
    new_menu = """"""
    keys = list(topic_dict.keys())
    clear()
    last_index = 0
    for i, topic in enumerate(topic_dict.items()):
        new_menu += f"{i+1}. {'[X]' if topic[1] else '[ ]'} {topic[0]} \n"
        last_index = i + 1
    new_menu += f"{last_index+1}. Back \nChoice: "
    response = int_input_getter(new_menu, range(1, last_index+2))
    if response == last_index+1:
        return
    else:
        webbrowser.open(links[keys[response-1]])
        mark_complete = yes_or_no_handler("Would you like to mark that topic complete?(y/n): ")
        if mark_complete.__eq__("y"):
            topics[cat_name][keys[response-1]] = True


def view_progress():
    """
    This function displays the total completion and the individual completion of all domains.
    :return: None
    """
    clear()
    total_topics = 327  # 327 is the total number of acronyms
    num_completed = 0
    cats = ['GSC', 'TVM', 'SA', 'SO', 'SPMaO']
    for cat in cats:
        total_topics += len(topics[cat])
        for topic in topics[cat].values():
            if topic:
                num_completed += 1
    for acronym in acronyms.values():
        if acronym[2]:
            num_completed += 1
    if num_completed == 446:
        print("CONGRATULATIONS! YOU'RE READY TO TAKE YOUR TEST!")
    print(f"""Progress Report:
General Security Concepts ({get_progress(topics['GSC'])})%
Threats, Vulnerabilities, and Mitigations ({get_progress(topics["TVM"])})%
Security Architecture ({get_progress(topics["SA"])})%
Security Operations ({get_progress(topics["SO"])})%
Security Program Management and Oversight ({get_progress(topics["SPMaO"])})%
Acronyms ({get_progress(acronyms)})%
TOTAL: {(num_completed/total_topics)*100:.2f}%
""")
    input("Press enter to continue...")


def get_progress(topic_dict):
    """
    This function gets the individual progress of the selected topic domain.
    :param topic_dict: (dict) The dictionary of topics
    :return: (float) a number with an accuracy of 2 decimal points
    """
    dict_len = len(topic_dict)
    num_completed = 0
    if isinstance(list(topic_dict.values())[0], bool):
        for topic in topic_dict.values():
            if topic:
                num_completed += 1
        return f"{(num_completed/dict_len)*100:.2f}"
    else:
        for topic in topic_dict.values():
            if topic[2]:
                num_completed += 1
        return f"{(num_completed/dict_len)*100:.2f}"


def save():
    """
    This function saves the user's data back to the JSON files.
    :return: None
    """
    files = ["data/(1)GSC.json", "data/(2)TVM.json", "data/(3)SA.json", "data/(4)SO.json", "data/(5)SPMaO.json"]
    for file in files:
        with open(file, "w") as json_file:
            json.dump(topics[file[8:-5]], json_file, indent=4)
    with open("data/acronyms.json", "w") as acronym_file:
        json.dump(acronyms, acronym_file, indent=4)


if __name__ == '__main__':
    main()
