import json
import random
import os
import webbrowser
from colorama import Fore, Style

def load_tally(filename='tally.json'):
    print("Loading tally...")  # Debug print
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r') as file:
        return json.load(file)

def save_tally(tally, filename='tally.json'):
    print("Saving tally...")  # Debug print
    with open(filename, 'w') as file:
        json.dump(tally, file)

def load_questions(filename='questions.json'):
    print("Loading questions...")  # Debug print
    with open(filename, 'r') as file:
        return json.load(file)

def shuffle_answers(options):
    random.shuffle(options)
    return options

def display_question_and_options(question, options, image_url=None):
    print(question)
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option['text']}")
    if image_url:
        webbrowser.open(image_url)

def get_user_choices(num_options):
    choices = input("Your answers (e.g., 1,3,4): ").split(',')
    try:
        choices = [int(choice.strip()) for choice in choices]
        if all(1 <= choice <= num_options for choice in choices):
            return choices
        else:
            print("Invalid choice(s). Please select valid options.")
            return get_user_choices(num_options)
    except ValueError:
        print("Please enter numbers separated by commas.")
        return get_user_choices(num_options)

def check_answers(options, choices):
    correct_indices = [idx for idx, opt in enumerate(options, start=1) if opt['correct']]
    return sorted(choices) == sorted(correct_indices)

def write_failed_question_to_file(failed_question, q_data, filename='failed_questions.txt'):
    with open(filename, 'a+') as file:
        file.write(failed_question + '\n' + q_data + '\n\n')

def main():
    print("Starting main function...")  # Debug print
    print("Loading questions...")  # Debug print
    questions = load_questions()
    print("Questions loaded.")  # Debug print
    asked_questions = set()
    tally = load_tally()
    print("Tally loaded.")  # Debug print

    while True:
        if len(asked_questions) == len(questions) or len(asked_questions) == 5:
            print("You've gone through all the questions or reached the limit. Good job!")
            break

        title, q_data = random.choice([item for item in questions.items() if item[0] not in asked_questions])
        asked_questions.add(title)
        shuffled_options = shuffle_answers(q_data['options'])

        if title not in tally:
            tally[title] = {'correct': 0, 'incorrect': 0}
        print('\n')
        display_question_and_options(q_data['question'], shuffled_options, q_data.get('image_url'))

        user_choices = get_user_choices(len(shuffled_options))
        if check_answers(shuffled_options, user_choices):
            print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
            tally[title]['correct'] += 1
        else:
            print(Fore.RED + "Incorrect. Better luck next time!" + Style.RESET_ALL)
            for option in q_data['options']:
                if option['correct']:
                    print(Fore.RED + "The correct answer was: ", option['text'] + Style.RESET_ALL)
            write_failed_question_to_file(title, q_data['question'])
            tally[title]['incorrect'] += 1
            if tally[title]['incorrect'] > 1:
                print("Uh oh, you've missed this question more than once")
                print('Number of times failed:', tally[title]['incorrect'])
            continue
        save_tally(tally)

        # Ask the user if they want to continue
        answer = input("Would you like to continue with another set of questions? (Y/N): ").strip().lower()
        if answer != 'y':
            print("Exiting the quiz. Goodbye!")
            break

if __name__ == "__main__":
    main()
