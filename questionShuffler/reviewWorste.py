import json
import os
import random

def load_tally(filename='tally.json'):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r') as file:
        return json.load(file)
    
def save_tally(tally, filename='tally.json'):
    with open(filename, 'w') as file:
        json.dump(tally, file)
    
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

def main():
    questions = load_questions()
    asked_questions = set()
    tally = load_tally()

    # Calculate failure rate for each question
    failure_rates = {}
    for title in questions.keys():
        total_attempts = tally.get(title, {}).get('correct', 0) + tally.get(title, {}).get('incorrect', 0)
        if total_attempts > 0:
            failure_rates[title] = tally.get(title, {}).get('incorrect', 0) / total_attempts
        else:
            failure_rates[title] = 0

    # Sort questions based on failure rate in descending order
    sorted_questions = sorted(questions.items(), key=lambda x: failure_rates.get(x[0], 0), reverse=True)
    while True:
        if len(asked_questions) == len(questions) or len(asked_questions) == 5:
            print("You've gone through all the questions or reached the limit. Good job!")
            break

        # Select the first question from the sorted list that hasn't been asked yet
        for title, q_data in sorted_questions:
            if title not in asked_questions:
                break

        asked_questions.add(title)
        shuffled_options = shuffle_answers(q_data['options'])
        
        print('\n')
        ## Tell the user how many times they've failed the question
        print(f"You've failed this question {tally[title]['incorrect']} times and gotten it right {tally[title]['correct']} times.")
        display_question_and_options(q_data['question'], shuffled_options)
        
        user_choices = get_user_choices(len(shuffled_options))
        if check_answers(shuffled_options, user_choices):
            print("Correct!")
            tally[title]['correct'] += 1
        else:
            print("Incorrect. Better luck next time!")
            tally[title]['incorrect'] += 1
            for option in q_data['options']:
                if option['correct']:
                    print("The correct answer was: ", option['text'])
            continue
        total_correct = sum(tally[title]['correct'] for title in tally)
        total_questions = total_correct + sum(tally[title]['incorrect'] for title in tally)
        percentage_correct = (total_correct / total_questions) * 100
        print(f"Your running percentage of correct answers is: {percentage_correct:.2f}%")
        save_tally(tally)
        
if __name__ == "__main__":
    main()