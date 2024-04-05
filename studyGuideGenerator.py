import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv('OPEN_AI')

def generate_study_guide():
    
    print("working on it...")
    
    with open('questionShuffler/failed_questions.txt', 'r') as file:
        failed_questions = file.read()
    
    prompt = (
        f"I answered the following questions incorrectly.\n"
        f"Can you create a short intuitive guide as to how I could find the right answer?\n"
        f"Answers should be concise and to the point, and also in the form:\n"
        f"Problem: \n"
        f"Concepts: \n"
        f"Steps to solve: \n"
        f"Easy way to remember: \n"
        f"I'll tip you $200 if you do a good job. Generate the study guide in .md format.\n"
        f"{failed_questions}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": "You are an expert teach of AWS."},
                {"role": "user", "content": prompt}
            ]
        )
        
        with open('study_guide.md', 'w') as output_file:
            output_file.write(response['choices'][0]['message']['content'])
            print("Study guide generated successfully!")
    
    except Exception as e:
        print(f"Error generating study guide: {str(e)}")



generate_study_guide()