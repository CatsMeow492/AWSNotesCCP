import json
import random

def load_questions(filename='questions.json'):
    with open(filename, 'r') as file:
        return json.load(file)

def shuffle_answers(options):
    random.shuffle(options)
    return options

def display_question_and_options(question, options):
    print(question)
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option['text']}")

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
    questions = load_questions()
    asked_questions = set()

    while True:
        if len(asked_questions) == len(questions) or len(asked_questions) == 5:
            print("You've gone through all the questions or reached the limit. Good job!")
            break

        title, q_data = random.choice([item for item in questions.items() if item[0] not in asked_questions])
        asked_questions.add(title)
        shuffled_options = shuffle_answers(q_data['options'])
        
        print(title)
        display_question_and_options(q_data['question'], shuffled_options)
        
        user_choices = get_user_choices(len(shuffled_options))
        if check_answers(shuffled_options, user_choices):
            print("Correct!")
        else:
            print("Incorrect. Better luck next time!")
            write_failed_question_to_file(title, q_data['question'])
            continue

if __name__ == "__main__":
    main()
