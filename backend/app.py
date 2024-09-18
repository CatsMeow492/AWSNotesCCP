from flask import Flask, request, jsonify
import json
import random
import os

app = Flask(__name__)

def load_questions(filename='questions.json'):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r') as file:
        return json.load(file)

def shuffle_answers(options):
    random.shuffle(options)
    return options

questions = load_questions()

@app.route('/questions', methods=['GET'])
def get_questions():
    question_list = []
    for q_key, q_data in questions.items():
        question_list.append({
            'id': q_key,
            'question': q_data['question'],
            'options': shuffle_answers(q_data['options']),
            'image_url': q_data.get('imageUrl')
        })
    return jsonify(question_list)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    question_id = data['question_id']
    user_choices = data['choices']
    
    correct_indices = [idx for idx, opt in enumerate(questions[question_id]['options'], start=1) if opt['correct']]
    is_correct = sorted(user_choices) == sorted(correct_indices)
    
    return jsonify({'correct': is_correct})

if __name__ == '__main__':
    app.run(debug=True)
